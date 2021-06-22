import pymongo


class ScrapeDB():

    def __init__(self):
        client = pymongo.MongoClient("mongodb://scraper:password@188.166.233.97/scrape_db")
        self.db = client.scrape_db.web_scrape

    def insert(self, data:dict) -> bool:
        try:
            # Insert dictionary
            self.db.insert_one(data)

            # Jika tidak ada error kembalikan True
            return True
        except Exception as e:
            # Mencetak pesan error ke console
            print(e)
            
            # Jika ada error kembalikan False
            return False

