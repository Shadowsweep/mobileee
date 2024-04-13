import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape mobile phone data from a website
def scrape_mobile_data(url, name_class, price_class):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    phones = []
    prices = []
    links = []  # to store links
    
    # Scraping phone names, prices, and links
    phone_blocks = soup.find_all('a', class_='_1fQZEK')
    for block in phone_blocks:
        phones.append(block.find('div', class_=name_class).text.strip())
        prices.append(block.find('div', class_=price_class).text.strip())
        links.append("https://www.flipkart.com" + block['href'])  # Constructing absolute links
    
    return phones, prices, links

# Function to append data to CSV file
def append_to_csv(file_name, data):
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Function to get the maximum number of smartphones on Flipkart
def get_max_smartphones(url, name_class, price_class):
    total_phones = 0
    page_num = 1
    all_data = [["Phone", "Price", "Mobile Link"]]  # Header for CSV
    while True:
        page_url = f"{url}&page={page_num}"
        phones, prices, links = scrape_mobile_data(page_url, name_class, price_class)
        if not phones:
            break
        for phone, price, link in zip(phones, prices, links):
            all_data.append([phone, price, link])  # Append data to list
            print(f"Phone: {phone}, Price: {price}, Link: {link}")  # Print for verification
        total_phones += len(phones)
        page_num += 1
    
    # Append data to CSV
    append_to_csv("mobile_data.csv", all_data)
    return total_phones

# Scrape Flipkart mobile data
flipkart_url = 'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree'
flipkart_name_class = '_4rR01T'
flipkart_price_class = '_30jeq3 _1_WHN1'
max_flipkart_phones = get_max_smartphones(flipkart_url, flipkart_name_class, flipkart_price_class)

print("Maximum smartphones on Flipkart:", max_flipkart_phones)
