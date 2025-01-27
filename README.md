# 🚀 Daraz Product Scraper
 This script uses Selenium library to scrape product details, including title, price, product description, rating, number of reviews, and user reviews from a Daraz product page.

## 📌 Workflow
- Scrolls to the bottom of the webpage to ensure dynamic content loads properly.
- Extracts the following product information:
    - Product title
    - Product price
    - Product description
    - Average rating
    - Number of reviews
    - List of user reviews 

## Code Breakdown
**Chrome Options:** 

Disables caching for better consistency when scraping dynamic pages.

**Scrolling:**

JavaScript window.scrollTo is used to scroll to the bottom of the page to load additional content.

**Data Extraction:**

CLASS_NAME: Used to scrape elements like the product title and user reviews.
CSS_SELECTOR: Used to extract elements such as the price, product description, rating and the number of reviews.
