import os
import time
import functools
from constants import AUTH_TOKEN
from fastapi import HTTPException
from notification import EmailNotifier

EMAIL_NOTIFIER = EmailNotifier(
    smtp_server=os.environ.get("SMTP_SERVER"),
    smtp_port=os.environ.get("SMTP_PORT"),
    username=os.environ.get("SMTP_USERNAME"),
    password=os.environ.get("SMTP_PASSWORD"),
    from_email=os.environ.get("SMTP_USERNAME"),
)


def get_token_header(x_token: str):
    if x_token != AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")


def retry(retries=3, delay=5):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    time.sleep(delay)
                    print(f"Retrying due to error: {e}")
            raise Exception("Max retries reached")

        return wrapper

    return decorator
