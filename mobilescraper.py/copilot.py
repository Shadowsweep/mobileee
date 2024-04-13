import requests
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

# Scrape Flipkart mobile data
flipkart_url = 'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree&page=1'
flipkart_name_class = '_4rR01T'
flipkart_price_class = '_30jeq3 _1_WHN1'
flipkart_phones, flipkart_prices = scrape_mobile_data(flipkart_url, flipkart_name_class, flipkart_price_class)

# Scrape Amazon mobile data
amazon_url = 'https://www.amazon.com/s?k=mobile+phones'
amazon_name_class = 'a-size-medium a-color-base a-text-normal'
amazon_price_class = 'a-price-whole'
amazon_phones, amazon_prices = scrape_mobile_data(amazon_url, amazon_name_class, amazon_price_class)

# Print Flipkart data
print("Flipkart Mobiles:")
for phone, price in zip(flipkart_phones, flipkart_prices):
    print(f"Phone: {phone}, Price: {price}")

# Print Amazon data
print("\nAmazon Mobiles:")
for phone, price in zip(amazon_phones, amazon_prices):
    print(f"Phone: {phone}, Price: ${price}")
