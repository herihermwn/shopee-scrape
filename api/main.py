import json
import requests
import logging
from config import *
from bottle import run, post, Bottle, request, response
from datetime import datetime


def runSpider():
    # Load passing data from post
    postData = json.loads(request.body.read())
    # Data validation
    result = dataValidation(['keyword'], postData)
    
    if result['status'] is True:
        keyword = postData['keyword']

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
            product['item_price'] = i['item_basic']['price']
            product['item_rating_star'] = i['item_basic']['item_rating']['rating_star']
            product['is_official_shop'] = i['item_basic']['is_official_shop']
            product['shop_location'] = i['item_basic']['shop_location']
            product['shop_id'] = shop_id
            product['total_items_sold'] = i['item_basic']['historical_sold']
            
            products.append(product)
        
        result['data'] = products

    return result


def dataValidation(names: 'List of str', value: dict):
    result = {
        'status': True,
        'message': "Scrape completed"
    }

    for name in names:
        if name not in value:
            result = {
                'status': False,
                'message': "The {} cannot be empty".format(name)
            }

    return result

if __name__ == '__main__':
    app = Bottle()

    @app.post('/runspider')
    def run_spider():
        response.content_type = 'application/json'
        return runSpider()

    app.run(host=API_HOST, port=API_PORT, debug=API_DEBUG)
