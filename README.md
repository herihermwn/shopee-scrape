# Shopee-scrape

## Install
    
    python3 -m venv .venv
    python3 -m pip install requests
    python3 -m pip install flask
    python3 -m pip install pymongo
    export FLASK_ENV=development
    export FLASK_APP=main.py

## Run

    source .venv/bin/activate (When you're finished with your virtual environment, enter the following command to deactivate it: deactivate)
    python3 shopee.py

## Database

    DB Name : scrape_db <br>
    HOST: 188.166.233.97 <br>
    PORT: 27017 <br>
    USER: scraper <br>
    PASSWORD: password <br>

## Sample connect to Database

    mongo -u scraper -p password 188.166.233.97/scrape_db