import pandas as pd
import re

# Load your 10-row scraped CSV
df = pd.read_csv("scraped_vehicles.csv")

def process_automotive_price(price_str, strategy='min'):
    if pd.isna(price_str) or price_str == "N/A":
        return None
        
    price_str = str(price_str).upper()
    
    # Find valid numbers/decimals only (prevents isolated dots from breaking it)
    found_matches = re.findall(r'\d+\.\d+|\d+', price_str)
    numbers = [float(x) for x in found_matches]
    
    if not numbers:
        return None
        
    # 2. Apply the chosen range strategy
    if len(numbers) == 2:
        if strategy == 'min':
            val = numbers[0]
        elif strategy == 'max':
            val = numbers[1]
        else: # average
            val = sum(numbers) / 2
    else:
        val = numbers[0]
        
    # 3. Apply the unit multiplier
    if 'LAKH' in price_str:
        return int(val * 100000)
    elif 'CRORE' in price_str or 'CR' in price_str:
        return int(val * 10000000)
    
    return int(val)

# Apply the logic to create a pristine numeric column
df['Clean_Price_INR'] = df['Raw_Price'].apply(lambda x: process_automotive_price(x, strategy='min'))

# Save the dataset ready for your dashboard
df.to_csv("cleaned_vehicles.csv", index=False)
print("Data parsing complete! Preview:")
print(df[['Model_Name', 'Raw_Price', 'Clean_Price_INR']])

 # --- FEATURE ENGINEERING ---
print("Starting feature engineering...")

# 1. Extract the Brand (Manufacturer)
# Assuming the first word of the 'Model_Name' is the brand (e.g., "Honda ZR-V" -> "Honda")
def extract_brand(name):
    if pd.isna(name) or name == "N/A":
        return "Unknown"
    # Split the string by spaces and grab the very first word
    return str(name).split()[0].upper()

df['Brand'] = df['Model_Name'].apply(extract_brand)

# 2. Create Market Price Segments
# Define our bin edges in Rupees and their corresponding labels
price_bins = [0, 1000000, 2000000, 4000000, float('inf')]
segment_labels = ['Budget (Under 10L)', 'Mid-Range (10L-20L)', 'Premium (20L-40L)', 'Luxury (40L+)']

# Use pd.cut() to sort the clean prices into these buckets automatically
df['Market_Segment'] = pd.cut(df['Clean_Price_INR'], bins=price_bins, labels=segment_labels)

# --- FINAL EXPORT ---
# Reorder the columns so they look clean in our BI tool
final_columns = ['Brand', 'Model_Name', 'Raw_Price', 'Clean_Price_INR', 'Market_Segment']
df = df[final_columns]

# Save the ultimate version ready for the dashboard
df.to_csv("dashboard_ready_vehicles.csv", index=False)

print("\nSuccess! Feature Engineering complete.")
print("Here is a preview of your final dataset:")
print(df.head())