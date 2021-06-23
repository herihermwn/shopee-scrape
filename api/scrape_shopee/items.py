# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BaseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    keyword = scrapy.Field()
    created_at = scrapy.Field()
    data = scrapy.Field()

class ScrapeShopeeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_item = scrapy.Field()
    photo_url_item = scrapy.Field()
    stock_item = scrapy.Field()
    brand_item = scrapy.Field()
    price_item = scrapy.Field()
    rating_star_item = scrapy.Field()
    is_official_shop = scrapy.Field()
    shop_location = scrapy.Field()
    total_items_sold = scrapy.Field()

