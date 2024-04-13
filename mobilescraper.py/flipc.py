import requests
import csv
from bs4 import BeautifulSoup

# Function to scrape mobile phone data from a website
def scrape_mobile_data(url, name_class, price_class):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    phones = []
    prices = []
    
    # Scraping phone names
    phone_names = soup.find_all('div', class_=name_class)
    for name in phone_names:
        phones.append(name.text.strip())
    
    # Scraping phone prices
    phone_prices = soup.find_all('div', class_=price_class)
    for price in phone_prices:
        prices.append(price.text.strip())
    
    return phones, prices

# Function to get the maximum number of smartphones on Flipkart
def get_max_smartphones(url, name_class, price_class):
    total_phones = 0
    page_num = 1
    with open('flipkart_smartphones.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price'])  # Write header
        while True:
            page_url = f"{url}&page={page_num}"
            phones, prices = scrape_mobile_data(page_url, name_class, price_class)
            if not phones:
                break
            for phone, price in zip(phones, prices):
                writer.writerow([phone, price])
            total_phones += len(phones)
            page_num += 1
    return total_phones

# Scrape Flipkart mobile data
flipkart_url = 'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree'
flipkart_name_class = '_4rR01T'
flipkart_price_class = '_30jeq3 _1_WHN1'
max_flipkart_phones = get_max_smartphones(flipkart_url, flipkart_name_class, flipkart_price_class)

print("Maximum smartphones on Flipkart:", max_flipkart_phones)
