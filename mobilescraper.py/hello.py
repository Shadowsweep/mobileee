import asyncio
import aiohttp
from bs4 import BeautifulSoup
import csv
import random
import time

# Function to scrape mobile phone data from a website asynchronously
async def scrape_mobile_data_async(url, headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')
                phones = []
                prices = []
                links = []
                images = []
                phone_blocks = soup.find_all('a', class_='_1fQZEK')
                for block in phone_blocks:
                    phones.append(block.find('div', class_=name_class).text.strip())
                    prices.append(block.find('div', class_=price_class).text.strip())
                    links.append("https://www.flipkart.com" + block['href'])
                    images.append(block.find('img', class_='_396cs4')['src'])
                return phones, prices, links, images
            else:
                return [], [], [], []

# Function to fetch maximum smartphones asynchronously
async def get_max_smartphones_async(url, name_class, price_class):
    total_phones = 0
    page_num = 1
    all_data = []
    headers = ["Phone", "Price", "Mobile Link", "Brand", "Color", "Storage", "Image URL"]
    while True:
        page_url = f"{url}&page={page_num}"
        phones, prices, links, images = await scrape_mobile_data_async(page_url, headers)
        if not phones:
            break
        brands = fetch_brand_names(phones)
        colors, storage = fetch_colors_and_storage_from_phones("mobile_data.csv")
        for phone, price, link, brand, color, storage_info, image_url in zip(phones, prices, links, brands, colors, storage, images):
            all_data.append([phone, price, link, brand, color, storage_info, image_url])
            print(f"Phone: {phone}, Price: {price}, Link: {link}, Brand: {brand}, Color: {color}, Storage: {storage_info}, Image URL: {image_url}")
        total_phones += len(phones)
        page_num += 1
        await asyncio.sleep(random.uniform(1, 3))  # Introduce random delay between requests
    append_to_csv("mobile_data6.csv", all_data, headers)
    return total_phones

# Update the User-Agent list with a variety of user agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    # Add more user agents here...
]

# Randomize the User-Agent selection
headers = {'User-Agent': random.choice(user_agents)}

# Scrape Flipkart mobile data asynchronously
flipkart_url = 'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree'
flipkart_name_class = '_4rR01T'
flipkart_price_class = '_30jeq3 _1_WHN1'

loop = asyncio.get_event_loop()
max_flipkart_phones = loop.run_until_complete(get_max_smartphones_async(flipkart_url, flipkart_name_class, flipkart_price_class))

print("Maximum smartphones on Flipkart:", max_flipkart_phones)
