from pymongo import MongoClient
from typing import List, Dict
import os


class Database:
    def __init__(self, db_name="scraping_db", collection_name="products"):
        self.client = MongoClient(
            os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
        )
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def save_products(self, products: List[Dict]):
        for product in products:
            self.collection.update_one(
                {"product_title": product["product_title"]},
                {"$set": product},
                upsert=True,
            )

    def load_products(self):
        return list(self.collection.find())
