import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_flipkart_data():
    url = "https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        product_cards = soup.find_all("div", class_="_1AtVbE")
        mobiles_data = []
        for card in product_cards:
            name = card.find("div", class_="_4rR01T").text
            price = card.find("div", class_="_30jeq3 _1_WHN1").text
            ram = card.find("li", class_="rgWa7D").text.split("|")[0].strip()
            brand = card.find("div", class_="_4rR01T").text.split()[0]
            mobiles_data.append({
                "Mobile Name": name,
                "Price": price,
                "RAM": ram,
                "Brand": brand,
            })
        return mobiles_data
    else:
        print("Failed to retrieve data from Flipkart.")
        return None

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("flipkart_mobiles.csv", index=False)
    print("Data saved to flipkart_mobiles.csv")

if __name__ == "__main__":
    mobile_data = get_flipkart_data()
    if mobile_data:
        save_to_csv(mobile_data)
