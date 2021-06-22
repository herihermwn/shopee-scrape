import json
import scrapy
from datetime import datetime
from urllib.parse import urlencode
from app.scrape_shopee.items import ScrapeShopeeItem, BaseItem

class ShopeeSpiderSpider(scrapy.Spider):
    name = 'shopee_spider'
    allowed_domains = ['shopee.co.id']

    def __init__(self, keyword: str):
        self.keyword = keyword


    def start_requests(self):
        params = (
            ('by', 'relevancy'),
            ('keyword', self.keyword),
            ('limit', '100'),
            ('newest', '0'),
            ('official_mall', '1'),
            ('order', 'desc'),
            ('page_type', 'search'),
            ('scenario', 'PAGE_MALL_SEARCH'),
            ('version', '2'),
        )
        url = 'https://shopee.co.id/api/v4/search/search_items?'

        yield scrapy.Request(url + urlencode(params), callback=self.parse)


    def parse(self, response):
        json_obj = json.loads(response.text)
        base_item = BaseItem()
        items = []

        for i in json_obj['items']:
            item = ScrapeShopeeItem()
            item['name_item'] = i['item_basic']['name']
            item['photo_url_item'] = 'https://cf.shopee.co.id/file/{}'.format(i['item_basic']['image'])
            item['stock_item'] = i['item_basic']['stock']
            item['brand_item'] = i['item_basic']['brand']
            item['price_item'] = i['item_basic']['price']
            item['rating_star_item'] = i['item_basic']['item_rating']['rating_star']
            item['is_official_shop'] = i['item_basic']['is_official_shop']
            item['shop_location'] = i['item_basic']['shop_location']
            item['total_items_sold'] = i['item_basic']['historical_sold']

            items.append(item)
        
        base_item['keyword'] = self.keyword
        base_item['created_at'] = datetime.now()
        base_item['data'] = items

        yield base_item