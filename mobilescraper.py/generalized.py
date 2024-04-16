import requests
from bs4 import BeautifulSoup
import csv

def get_laptops(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    laptops = []
    seen_laptops = set()
    for laptop in soup.find_all('div', class_='_1AtVbE'):
        name_elem = laptop.find('div', class_='_4rR01T')
        price_elem = laptop.find('div', class_='_30jeq3 _1_WHN1')
        color_elem = laptop.find('a', class_='IRpwTa')
        buy_link_elem = laptop.find('a', class_='_1fQZEK')
        if name_elem:
            name = name_elem.text
        else:
            continue  # Skip this laptop if name is not available
        if name in seen_laptops:
            continue  # Skip this laptop if it's a duplicate
        else:
            seen_laptops.add(name)
        if price_elem:
            price = price_elem.text
        else:
            price = "Price not available"
        if color_elem:
            color = color_elem.text
        else:
            color = "Color not available"
        if buy_link_elem:
            buy_link = "https://www.flipkart.com" + buy_link_elem['href']
        else:
            buy_link = "Buy link not available"
        laptops.append({'Name': name, 'Price': price, 'Color': color, 'Buy Link': buy_link})
    return laptops

def get_smartphones(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    smartphones = []
    seen_smartphones = set()
    for smartphone in soup.find_all('div', class_='_1AtVbE'):
        name_elem = smartphone.find('div', class_='_4rR01T')
        price_elem = smartphone.find('div', class_='_30jeq3 _1_WHN1')
        color_elem = smartphone.find('a', class_='IRpwTa')
        buy_link_elem = smartphone.find('a', class_='_1fQZEK')
        if name_elem:
            name = name_elem.text
        else:
            continue  # Skip this smartphone if name is not available
        if name in seen_smartphones:
            continue  # Skip this smartphone if it's a duplicate
        else:
            seen_smartphones.add(name)
        if price_elem:
            price = price_elem.text
        else:
            price = "Price not available"
        if color_elem:
            color = color_elem.text
        else:
            color = "Color not available"
        if buy_link_elem:
            buy_link = "https://www.flipkart.com" + buy_link_elem['href']
        else:
            buy_link = "Buy link not available"
        smartphones.append({'Name': name, 'Price': price, 'Color': color, 'Buy Link': buy_link})
    return smartphones

def get_smartwatches(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    smartwatches = []
    seen_smartwatches = set()
    for smartwatch in soup.find_all('div', class_='_1AtVbE'):
        name_elem = smartwatch.find('a', class_='IRpwTa')
        price_elem = smartwatch.find('div', class_='_30jeq3 _1_WHN1')
        color_elem = smartwatch.find('a', class_='IRpwTa')
        buy_link_elem = smartwatch.find('a', class_='_1fQZEK')
        if name_elem:
            name = name_elem.text
        else:
            continue  # Skip this smartwatch if name is not available
        if name in seen_smartwatches:
            continue  # Skip this smartwatch if it's a duplicate
        else:
            seen_smartwatches.add(name)
        if price_elem:
            price = price_elem.text
        else:
            price = "Price not available"
        if color_elem:
            color = color_elem.text
        else:
            color = "Color not available"
        if buy_link_elem:
            buy_link = "https://www.flipkart.com" + buy_link_elem['href']
        else:
            buy_link = "Buy link not available"
        smartwatches.append({'Name': name, 'Price': price, 'Color': color, 'Buy Link': buy_link})
    return smartwatches

def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Price', 'Color', 'Buy Link'])
        writer.writeheader()
        for item in data:
            writer.writerow(item)

def main():
    choice = input("Choose an option:\n1. Smartwatches\n2. Smartphones\n3. Laptops\n")
    if choice == '1':
        base_url = 'https://www.flipkart.com/smart-watches/pr?sid=ajy,buh&otracker=categorytree'
        data = get_smartwatches(base_url)
        write_to_csv(data, 'flipkart_smartwatches.csv')
    elif choice == '2':
        base_url = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree'
        data = get_smartphones(base_url)
        write_to_csv(data, 'flipkart_smartphones.csv')
    elif choice == '3':
        base_url = 'https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree'
        data = get_laptops(base_url)
        write_to_csv(data, 'flipkart_laptops.csv')
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()
