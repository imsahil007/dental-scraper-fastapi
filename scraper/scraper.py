import requests
from bs4 import BeautifulSoup
from models import Product, ScrapeSettings
from settings.database import Database
from settings.cache import Cache
import os
from utils import retry

from notification import Notifier


class Scraper:
    def __init__(
        self,
        settings: ScrapeSettings,
        notifier: Notifier = None,
    ):
        self.settings = settings
        self.db = Database()
        self.cache = Cache()
        self.base_url = "https://www.google.com/"
        self.notifier = notifier

    @retry(retries=3, delay=5)
    def scrape(self):
        raise NotImplementedError("Method not implemented")

    def download_image(self, url):
        response = requests.get(url, verify=False)
        img_name = url.split("/")[-1]
        # root_path = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join("images", img_name)
        os.makedirs(os.path.dirname(img_path), exist_ok=True)
        with open(img_path, "wb") as f:
            f.write(response.content)
        return img_path

    def notify(self, num_products):
        message = f"{num_products} products scraped and saved."
        if self.notifier:
            if self.notifier.TYPE == "email":
                self.notifier.send(self.user, "Scraping Notification", message)
