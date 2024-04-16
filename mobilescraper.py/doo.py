from bs4 import BeautifulSoup
import csv
import requests

# Function to scrape mobile phone data from a website
def scrape_mobile_data(url, name_class, price_class, rating_class):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    phones = []
    prices = []
    links = []  # to store links
    ratings = []  # to store ratings
    
    # Scraping phone names, prices, links, and ratings
    phone_blocks = soup.find_all('a', class_='_1fQZEK')
    for block in phone_blocks:
        phones.append(block.find('div', class_=name_class).text.strip())
        prices.append(block.find('div', class_=price_class).text.strip())
        links.append("https://www.flipkart.com" + block['href'])  # Constructing absolute links
        rating = block.find('div', class_=rating_class)
        if rating:
            ratings.append(rating.text.strip())
        else:
            ratings.append('Not available')
    
    return phones, prices, links, ratings

# Function to append data to CSV file
def append_to_csv(file_name, data, headers):
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write headers
        writer.writerows(data)

# Function to fetch brand names from phone names
def fetch_brand_names(phones):
    return [phone.split(' ')[0] for phone in phones]

# Function to fetch colors and storage from phone names in CSV
def fetch_colors_and_storage_from_phones(file_name):
    colors = []
    storage = []
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming the color and storage are after the opening parenthesis '('
            phone_name = row['Phone']
            start_index = phone_name.find('(')
            end_index = phone_name.find(')')
            if start_index != -1 and end_index != -1:
                info = phone_name[start_index + 1:end_index].split(',')
                if len(info) >= 2:
                    color = info[0].strip()
                    storage_info = info[1].strip()
                    colors.append(color)
                    storage.append(storage_info)
                else:
                    colors.append(info[0].strip())
                    storage.append('Not available')
            else:
                colors.append('Not available')
                storage.append('Not available')
    return colors, storage

# Function to fetch ratings from phone data
def fetch_ratings(phones, url, rating_class):
    ratings = []
    for phone in phones:
        response = requests.get(url + phone.replace(" ", "-"), headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        rating_block = soup.find('div', class_=rating_class)
        if rating_block:
            rating = rating_block.text.strip()
            ratings.append(rating)
        else:
            ratings.append('Not available')
    return ratings

# Function to get the maximum number of smartphones on Flipkart
def get_max_smartphones(url, name_class, price_class, rating_class):
    total_phones = 0
    page_num = 1
    all_data = []  # List to hold all data
    headers = ["Phone", "Price", "Mobile Link", "Brand", "Color", "Storage", "Rating"]  # Header for CSV
    while True:
        page_url = f"{url}&page={page_num}"
        phones, prices, links = scrape_mobile_data(page_url, name_class, price_class, rating_class)
        if not phones:
            break
        brands = fetch_brand_names(phones)
        colors, storage = fetch_colors_and_storage_from_phones("mobile_data.csv")
        ratings = fetch_ratings(phones, url, rating_class)
        for phone, price, link, brand, color, storage_info, rating in zip(phones, prices, links, brands, colors, storage, ratings):
            all_data.append([phone, price, link, brand, color, storage_info, rating])  # Append data to list
            print(f"Phone: {phone}, Price: {price}, Link: {link}, Brand: {brand}, Color: {color}, Storage: {storage_info}, Rating: {rating}")  # Print for verification
        total_phones += len(phones)
        page_num += 1
    
    # Append data to CSV
    append_to_csv("mobile_datp.csv", all_data, headers)
    return total_phones

# Scrape Flipkart mobile data
flipkart_url = 'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree'
flipkart_name_class = '_4rR01T'
flipkart_price_class = '_30jeq3 _1_WHN1'
flipkart_rating_class = '._1lRcqv'
max_flipkart_phones = get_max_smartphones(flipkart_url, flipkart_name_class, flipkart_price_class, flipkart_rating_class)

print("Maximum smartphones on Flipkart:", max_flipkart_phones)
