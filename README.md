# DentalStall Scraper Tool

## Overview
The DentalStall Scraper Tool is a Python-based application developed to automate the process of scraping product information from the DentalStall online shop. Utilizing the FastAPI framework, this tool efficiently extracts product names, prices, and images from the catalogue pages without the need to open each product card individually. The scraped data is stored locally as a JSON file, with flexibility built into the design for easy adaptation to other storage strategies.



## Features
- **Selective Scraping:** Ability to limit the scraping process to a specified number of pages.
- **Proxy Support:** Option to use a proxy for scraping, enhancing privacy and bypassing potential scraping blocks.
- **Local Storage:** Scraped data is stored in a JSON format on the local storage, with an easy option to switch to other storage methods.
- **Notification System:** At the end of each scraping cycle, the tool notifies designated recipients about the number of products scraped and updated in the database, with flexibility for different notification strategies.
- **Data Integrity:** Ensures type validation and data integrity using appropriate methods for efficient data processing.
- **Retry Mechanism:** Implements a simple retry mechanism for handling server errors during the scraping process.
- **Authentication:** Secures the endpoint with simple authentication using a static token.
- **Caching:** Utilizes an in-memory database for caching scraping results, avoiding unnecessary updates for products whose prices have not changed.

## API Endpoints

- `POST /scrape`: Initiates the scraping process for a specified number of pages or products.


## Environment variables
```
SMTP_USERNAME="deployprojects@gmail.com" 
SMTP_PASSWORD=''
DENTAL_BASE_URL="https://dentalstall.com/shop/"
SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=587
```

## Setup and Local Execution

1. Clone the repository: `git clone https://github.com/imsahil007/dental-scraper-fastapi.git`
2. Navigate to the project directory: `cd dental-scraper-fastapi`
3. Install the dependencies: `pip install -r requirements.txt`
4. Set env params: `set -a && source .env`
5. Run the application: `uvicorn settings.main:app --reload`

This will start the FastAPI application, and you can access the documentation of the API by navigating to `http://127.0.0.1:8000/docs` in your web browser.

### Configuration
Before running the scraper, ensure to configure the following settings in the `config.json` file:
- `pages`: The maximum number of pages to scrape. Takes integer input
- `proxy`: The proxy string to use for scraping. Takes IP
- `x_token`: The static token for authenticating the endpoint. Takes value `some_static_token`. Gives 401
- `email`: Where you want to notify the user


## Swagger
```
http://localhost:8000/docs
```

## Docker Setup

The application can be easily containerized using Docker, simplifying deployment and execution.

To build and run the application in Docker:

1. Build the Docker image: `docker build -t dentalstall-scraper .`
2. Run the Docker container: `docker run -p 8000:8000 dentalstall-scraper`

