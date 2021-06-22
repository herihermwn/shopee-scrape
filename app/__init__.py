import requests
import json

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from pymongo import MongoClient

from config import app_config

with MongoClient("mongodb://scraper:password@188.166.233.97/scrape_db") as client:
    db = client.shopee_scrape

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # Route
    @app.route('/')
    def index():
        return 'Davi Ganteng!'

    @app.route('/search-item')
    def search_item():
        return render_template('search.html')

    @app.route('/list-item')
    def list_item():
        items = db.items.find()

        return render_template('list-item.html', items=items)

    @app.route('/search', methods=['GET'])
    def search():
        keyword = request.args.get('q', '')

        return searchItem(keyword)

    return app

def searchItem(keyword):
    params = (
        ('by', 'relevancy'),
        ('keyword', keyword),
        ('limit', '100'),
        ('newest', '0'),
        ('official_mall', '1'),
        ('order', 'desc'),
        ('page_type', 'search'),
        ('scenario', 'PAGE_MALL_SEARCH'),
        ('version', '2'),
    )

    response = requests.get('https://shopee.co.id/api/v4/search/search_items', params=params)
    result = json.loads(response.text)
    items = result['items']
    items = dataCleaning(items)

    return jsonify(items)

def dataCleaning(data):
    items = []

    for item in data:
        items.append({
            'name': item['item_basic']['name'],
            'price': item['item_basic']['price'],
            'brand': item['item_basic']['brand']
        })

    return items