import csv

# Function to fetch colors and storage from phone names in CSV
def fetch_colors_and_storage_from_phones(file_name):
    colors = []
    storage = []
    with open(file_name, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming the color is after the opening parenthesis '('
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

# Fetch and print colors and storage from CSV
csv_file = "mobile_data.csv"
colors, storage = fetch_colors_and_storage_from_phones(csv_file)
print("Colors and storage of mobiles:")
for color, storage_info in zip(colors, storage):
    print("Color:", color, ", Storage:", storage_info)
