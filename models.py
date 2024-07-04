from pydantic import BaseModel, EmailStr
from typing import List


class Product(BaseModel):
    product_title: str
    product_price: float
    path_to_image: str


class ScrapeSettings(BaseModel):
    pages: int = 1
    proxy: str = "207.180.252.79"
    email: EmailStr = "receive_notification_here@email.com"
