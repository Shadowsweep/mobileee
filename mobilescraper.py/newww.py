import csv

# Function to fetch brand names from CSV
def fetch_brand_names(file_name):
    brand_names = []
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming the phone names follow a pattern like "Brand Model"
            brand_name = row['Phone'].split(' ')[0]
            brand_names.append(brand_name)
    return brand_names

# Fetch and print brand names from CSV
csv_file = "mobile_data.csv"
brands = fetch_brand_names(csv_file)
print("Brand names of mobiles:")
for brand in brands:
    print(brand)
