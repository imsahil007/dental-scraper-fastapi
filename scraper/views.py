from requests import request
from scraper.dental_scraper import DentalScraper
from models import ScrapeSettings
from fastapi import APIRouter, Depends, HTTPException
from utils import get_token_header, EMAIL_NOTIFIER

router = APIRouter()


@router.post("/scrape", dependencies=[Depends(get_token_header)])
def scrape(settings: ScrapeSettings):
    """
    TOKEN: 'some_static_token'   

    SAMPLE PROXY: 207.180.252.79

    This endpoint scrapes the dental products from the website and saves them to the database. Called synchronously.

    You will receive an email notification when the scraping is done on the email provided in the payload
    
    """
    # user = request.user.email
    if settings.pages < 1:
        raise HTTPException(status_code=400, detail="Pages should be greater than 0")
    user = settings.email
    scraper = DentalScraper(settings, user, notifier=EMAIL_NOTIFIER)
    num_products = scraper.scrape()
    return {
        "status": f"{num_products} products scraped and saved. You will receive an email on {user}"
    }
