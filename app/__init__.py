import scrapy
from app.scrape_shopee.spiders.shopee_spider import ShopeeSpiderSpider

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

from config import app_config

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')

    # Route
    @app.route('/')
    def index():
        return 'Davi Ganteng!'

    @app.route('/search-item')
    def search_item():
        return render_template('search-item.html')

    @app.route('/list-item')
    def list_item():
        items = []

        return render_template('list-item.html', items=items)

    @app.route('/search', methods=['GET'])
    def search():
        keyword = request.args.get('q', '')
        spider = ShopeeSpiderSpider(keyword)

        items = spider.start_requests()

        # return items
        return keyword

    return app