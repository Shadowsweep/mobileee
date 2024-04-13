import csv

# Function to fetch colors from phone names in CSV
def fetch_colors_from_phones(file_name):
    colors = []
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming the color is after the opening parenthesis '('
            phone_name = row['Phone']
            start_index = phone_name.find('(')
            if start_index != -1:
                color = phone_name[start_index + 1:].split(',')[0]
                colors.append(color.strip())  # Remove leading/trailing whitespace
            else:
                colors.append('Not available')
    return colors

# Fetch and print colors from CSV
csv_file = "mobile_data.csv"
colors = fetch_colors_from_phones(csv_file)
print("Colors of mobiles:")
for color in colors:
    print(color)
