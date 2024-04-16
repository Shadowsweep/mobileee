import pandas as pd

# Load CSV into DataFrame
df = pd.read_csv('mobile_data.csv')

# Replace 'Not Available' with NaN
df.replace('Not Available', pd.NA, inplace=True)

# Drop rows with NaN values
df.dropna(inplace=True)

# Clean 'Price' column
df['Price'] = df['Price'].str.replace('₹', '').str.replace(',', '').astype(float)

# Clean 'Storage' column
df['Storage'] = df['Storage'].replace('Not available', pd.NA)
df.dropna(subset=['Storage'], inplace=True)  # Drop rows with NaN values in 'Storage'
df['Storage'] = df['Storage'].astype(int)

# Optionally, reset the index
df.reset_index(drop=True, inplace=True)

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_data.csv', index=False)

# Display the cleaned DataFrame
print(df)