import json
import requests

from config import *
from bottle import Bottle, request, response, template, static_file, redirect
from pymongo import MongoClient

import os, sys

dirname = os.path.dirname(sys.argv[0])

def runSpider(keyword=''):
    # Load passing data from post
    # postData = json.loads(request.body.read())
    # Data validation
    # result = dataValidation(['keyword'], postData)
    result = {
        'status': True,
        'message': "Scrape completed"
    }
    
    if keyword:
        params = {
            'by': 'relevancy',
            'keyword': keyword,
            'limit': '100',
            'newest': '0',
            'official_mall': '1',
            'order': 'desc',
            'page_type': 'search',
            'scenario': 'PAGE_MALL_SEARCH',
            'version': '2',
        }
        url = 'https://shopee.co.id/api/v4/search/search_items?'

        response = requests.get(url, params=params)
        json_obj = json.loads(response.text)

        products = []

        for i in json_obj['items']:
            product = {}
            
            item_id = i['item_basic']['itemid']
            item_name = i['item_basic']['name']
            shop_id = i['item_basic']['shopid']
            item_brand = i['item_basic']['brand']
            detail_url = 'https://shopee.co.id/{}-i.{}.{}'.format(item_name.replace(' ','-'), shop_id, item_id)

            if 'None' == item_brand:
                item_brand = None

            product['item_id'] = item_id
            product['item_name'] = item_name
            product['item_detail_url'] = detail_url
            product['item_photo_url'] = 'https://cf.shopee.co.id/file/{}'.format(i['item_basic']['image'])
            product['item_stock'] = i['item_basic']['stock']
            product['item_brand'] = item_brand
            product['item_price'] = i['item_basic']['price'] / 100000
            product['item_rating_star'] = i['item_basic']['item_rating']['rating_star']
            product['is_official_shop'] = i['item_basic']['is_official_shop']
            product['shop_location'] = i['item_basic']['shop_location']
            product['shop_id'] = shop_id
            product['total_items_sold'] = i['item_basic']['historical_sold']
            
            products.append(product)
        
        result['data'] = products

    return result

with MongoClient("mongodb://scraper:password@188.166.233.97/scrape_db") as client:
    db = client.scrape_db

if __name__ == '__main__':
    app = Bottle()

    @app.route('/static/<filename:path>')
    def send_static(filename):
        return static_file(filename, root=dirname+'/static')

    @app.route('/static/<filename:re:.*\.png>')
    def send_image(filename):
        return static_file(filename, root=dirname+'/static/img')

    @app.post('/runspider')
    def run_spider():
        response.content_type = 'application/json'
        keyword = request.forms.get('keyword')
        
        return runSpider(keyword)

    @app.route('/')
    def index():
        return template('index')

    @app.route('/items')
    def items():
        items = db.items.find()

        return template('item', items=items)

    @app.post('/items/create')
    def create():
        item = {
            "item_photo_url": request.forms.get('item_photo_url'),
            "item_id": request.forms.get('item_id'),
            "item_name": request.forms.get('item_name'),
            "item_detail_url": request.forms.get('item_detail_url'),
            "item_stock": request.forms.get('item_stock'),
            "item_brand": request.forms.get('item_brand'),
            "item_price": request.forms.get('item_price')
        }

        db.items.insert_one(item)

        redirect("/")

    @app.post('/items/<item_id>/delete')
    def destroy(item_id):
        db.items.delete_one({'item_id':item_id})

        redirect("/items")

    app.run(host=API_HOST, port=API_PORT, debug=API_DEBUG)
