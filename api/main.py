import json
import logging
from config import *
from bottle import run, post, Bottle, request, response
from scrape_shopee.spiders.shopee_spider import ShopeeSpiderSpider
from multiprocessing import Process, Manager
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from datetime import datetime


# Using CrawlerProcess will display the spider LOGGER
def getUserTweets(keyword):
    # Setting for spider
    settings = {
        'LOG_FILE': 'logs/logs-{}.txt'.format(datetime.now())
    }
    crawler = CrawlerProcess(settings=settings)

    # Set spider to CrawlerProcess & Passing parameter to Spider
    deferred = crawler.crawl(ShopeeSpiderSpider, keyword=keyword)
    deferred.addBoth(lambda _: reactor.stop())
    reactor.run()

    @deferred.addCallback
    def _success(results):
        """
        Do something when success
        """
        logging.info("Success")

    @deferred.addErrback
    def _error(failure):
        """
        Do something when error
        """
        logging.warning(failure.value)


# ===============================================
# Reference: https://stackoverflow.com/a/43661172/15503925
# ===============================================
def runSpider():
    # Load passing data from post
    postData = json.loads(request.body.read())
    # Data validation
    result = dataValidation(['keyword'], postData)
    
    if result['status'] is True:
        keyword = postData['keyword']

        process = Process(target=getUserTweets, args=[keyword])
        process.start()

        # ===============================================
        # Remove comment code bellow, response will
        # wait until the spider finish
        # ===============================================
        process.join()

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
        return runSpider()

    app.run(host=API_HOST, port=API_PORT, debug=API_DEBUG)
