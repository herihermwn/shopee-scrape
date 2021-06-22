# Shopee-scrape

## Install
    
    python3 -m venv .venv
    python3 -m pip install scrapy
    python3 -m pip install flask
    python3 -m pip install pymongo
    export FLASK_ENV=development
    export FLASK_CONFIG=development
    export FLASK_APP=main.py

## Run

    source .venv/bin/activate (When you're finished with your virtual environment, enter the following command to deactivate it: deactivate)
    scrapy runspider scrape_shopee/spiders/shopee_spider.py -a keyword='laptop'

## Database
    DB Name : scrape_db
    HOST: 188.166.233.97
    PORT: 27017
    USER: scraper
    PASSWORD: password

## Sample connect to Database
    mongo -u scraper -p password 188.166.233.97/scrape_db
