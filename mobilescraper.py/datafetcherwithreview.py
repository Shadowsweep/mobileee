from bs4 import BeautifulSoup
import csv
import requests

# Function to scrape mobile phone data from a website including reviews
def scrape_mobile_data_with_reviews(url, name_class, price_class, rating_class, review_class):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    phones = []
    prices = []
    links = []  # to store links
    ratings = []  # to store ratings
    reviews = []  # to store reviews
    
    # Scraping phone names, prices, links, ratings, and reviews
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
        review = block.find('div', class_=review_class)
        if review:
            reviews.append(review.text.strip())
        else:
            reviews.append('No reviews available')
    
    return phones, prices, links, ratings, reviews

# Function to append data to CSV file
def append_to_csv(file_name, data, headers):
    with open(file_name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write headers
        writer.writerows(data)

# Function to get the highest rated smartphone on Flipkart with reviews
def get_highest_rated_smartphone_with_reviews(url, name_class, price_class, rating_class, review_class):
    all_data = []  # List to hold all data
    headers = ["Phone", "Price", "Mobile Link", "Rating", "Reviews"]  # Header for CSV
    
    page_num = 1
    while True:
        page_url = f"{url}&page={page_num}"
        phones, prices, links, ratings, reviews = scrape_mobile_data_with_reviews(page_url, name_class, price_class, rating_class, review_class)
        if not phones:
            break
        for phone, price, link, rating, review in zip(phones, prices, links, ratings, reviews):
            all_data.append([phone, price, link, rating, review])  # Append data to list
            print(f"Phone: {phone}, Price: {price}, Link: {link}, Rating: {rating}, Reviews: {review}")  # Print for verification
        page_num += 1
    
    # Sort the data based on rating
    all_data.sort(key=lambda x: float(x[3]) if x[3] != 'Not available' else 0, reverse=True)
    
    # Append data to CSV
    append_to_csv("mobile_data_with_reviews_and_ratinl.csv", all_data, headers)
    
    # Return the highest rated smartphone
    if all_data:
        return all_data[0][3]  # Return the rating of the highest rated phone
    else:
        return 0  # Return 0 if no data is found

# Scrape Flipkart mobile data and find the highest rated smartphone with reviews
flipkart_url = 'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree'
flipkart_name_class = '_4rR01T'
flipkart_price_class = '_30jeq3 _1_WHN1'
flipkart_rating_class = '_3LWZlK'
flipkart_review_class = 't-ZTKy'
highest_rating = get_highest_rated_smartphone_with_reviews(flipkart_url, flipkart_name_class, flipkart_price_class, flipkart_rating_class, flipkart_review_class)
print("Rating of the highest rated smartphone on Flipkart:", highest_rating)
