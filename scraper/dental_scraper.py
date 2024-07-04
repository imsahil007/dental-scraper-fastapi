import requests
from bs4 import BeautifulSoup
from models import Product, ScrapeSettings
from settings.database import Database
from settings.cache import cache
import os
from utils import retry
from scraper.scraper import Scraper

from notification import Notifier


class DentalScraper(Scraper):
    def __init__(self, settings: ScrapeSettings, user: str, notifier: Notifier = None):
        self.settings = settings
        self.db = Database()
        self.base_url = os.environ.get(
            "DENTAL_BASE_URL", "https://dentalstall.com/shop/"
        )
        self.notifier = notifier
        self.user = user

    @retry(retries=3, delay=5)
    def scrape(self):
        products = []
        for page in range(1, self.settings.pages + 1):
            url = f"{self.base_url}/page/{page}"
            proxies = (
                {"http": self.settings.proxy, "https": self.settings.proxy}
                if self.settings.proxy
                else None
            )

            response = requests.get(url, proxies=proxies, verify=False)
            if response.status_code != 200:
                print(f"Failed to fetch page {page} status_code:{response.status_code}")
                continue

            soup = BeautifulSoup(response.content, "html.parser")
            for card in soup.select(".product-inner"):
                try:
                    product = card.select_one(".mf-product-details")
                    image = card.select_one(".mf-product-thumbnail")
                    title = product.select_one(".addtocart-buynow-btn").a["data-title"]
                    price = float(
                        product.select_one(".woocommerce-Price-amount")
                        .get_text(strip=True)
                        .replace("₹", "")
                    )
                    img_url = image.a.img.get("data-lazy-src")
                    img_path = self.download_image(img_url)
                    product_data = Product(
                        product_title=title, product_price=price, path_to_image=img_path
                    )
                    if not self.cache_product(
                        key=f"product:{title}", data=product_data
                    ):
                        continue

                except Exception as e:
                    print(f"Error scraping product: {e} url: {url}")
                    continue
                products.append(product_data.model_dump())
        self.db.save_products(products)
        self.notify(len(products))
        return len(products)

    def cache_product(self, key, data):
        cached_price = cache.get(key)
        if cached_price and float(cached_price) == data.product_price:
            return False
        cache.set(key, data.product_price)
        return True
