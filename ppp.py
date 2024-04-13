import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_mobile_specifications(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    specifications = []
    
    # Extracting relevant information
    brand_element = soup.find('span', {'class': 'brand'})
    brand = brand_element.text.strip() if brand_element else "N/A"
    
    name_element = soup.find('span', {'class': 'name'})
    name = name_element.text.strip() if name_element else "N/A"
    
    model_element = soup.find('span', {'class': 'model'})
    model = model_element.text.strip() if model_element else "N/A"
    
    ram_element = soup.find('span', {'class': 'ram'})
    ram = ram_element.text.strip() if ram_element else "N/A"
    
    storage_element = soup.find('span', {'class': 'storage'})
    storage = storage_element.text.strip() if storage_element else "N/A"
    
    price_element = soup.find('span', {'class': 'price'})
    price = price_element.text.strip() if price_element else "N/A"
    
    # Appending to the list
    specifications.append({
        'Brand': brand,
        'Mobile Name': name,
        'Model': model,
        'RAM': ram,
        'Storage': storage,
        'Price': price
    })
    
    return specifications

def export_to_csv(specifications, filename):
    df = pd.DataFrame(specifications)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    urls = [
        "https://www.tatacliq.com/smartphone-clp",
        "https://www.croma.com/",
        "https://www.flipkart.com/mobile-phones-store",
        # Add more URLs as needed
    ]
    
    all_specifications = []
    
    for url in urls:
        specifications = extract_mobile_specifications(url)
        all_specifications.extend(specifications)
    
    export_to_csv(all_specifications, 'mobile_specifications.csv')
