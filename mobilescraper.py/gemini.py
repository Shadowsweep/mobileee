import requests
import csv
from bs4 import BeautifulSoup

# Function to scrape mobile phone data from a website
def scrape_storage_data(url, name_class, storage_class):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    phones = []
    storage = []
    
    # Scraping phone names and storage data
    phone_data = soup.find_all('div', class_=name_class)
    for data in phone_data:
        phones.append(data.find('a').text.strip())
        specs = data.find_all('li', class_=storage_class)
        storage.append(specs[0].text.strip() if specs else 'N/A')
    
    return phones, storage

# Function to get the maximum number of smartphones on Flipkart
def get_max_smartphones(url, name_class, storage_class):
    total_phones = 0
    page_num = 1
    with open('flipkart_smartphones_storage.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Storage'])  # Write header
        while True:
            page_url = f"{url}&page={page_num}"
            phones, storage = scrape_storage_data(page_url, name_class, storage_class)
            if not phones:
                break
            for phone, store in zip(phones, storage):
                writer.writerow([phone, store])
            total_phones += len(phones)
            page_num += 1
    return total_phones

# Scrape Flipkart mobile data for storage
flipkart_url = 'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree'
flipkart_name_class = '_4rR01T'
flipkart_storage_class = 'rgWa7D'
max_flipkart_phones = get_max_smartphones(flipkart_url, flipkart_name_class, flipkart_storage_class)

print("Maximum smartphones on Flipkart:", max_flipkart_phones)
