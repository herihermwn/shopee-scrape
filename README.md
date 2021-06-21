# Shopee-scrape

## Install
    
    pip3 install scrapy
    pip3 install pymongo

## Run

    scrapy runspider scrape_shopee/spiders/shopee_spider.py -a keyword='laptop'

## Database
DB Name : scrape_db <br>
HOST: 188.166.233.97 <br>
PORT: 27017 <br>
USER: scraper <br>
PASSWORD: password <br>

## Sample connect to Database
    mongo -u scraper -p password 188.166.233.97/scrape_db
