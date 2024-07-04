from fastapi import FastAPI, Depends, HTTPException
from scraper.views import router

app = FastAPI()

AUTH_TOKEN = "your_static_token"


app.include_router(router)
