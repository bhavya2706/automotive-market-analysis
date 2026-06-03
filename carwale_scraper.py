import csv
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_automotive_data(url):
    # 1. Set up headers to mimic a real browser visit and avoid 403 Forbidden errors
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    print(f"Fetching page data from: {url}...")

    try:
        response = requests.get(url, headers=headers, timeout=10)
        # Raise an exception if the request returned an unsuccessful status code
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

    # 2. Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # List to store our extracted dictionaries
    vehicle_data = []

    # 3. Locate the parent containers for each vehicle card
    # NOTE: You must inspect your target website and update these class names.
    # For example, if each car is inside <div class="card-wrapper">, use that here.
    vehicle_cards = soup.find_all(
        "div", class_="o-bD o-kY o-mf o-lT o-mO o-n5 o-ne o-nn o-C")

    if not vehicle_cards:
        print("Warning: No vehicle cards found. Check if the class name or HTML structure matches the website.")
        return None

    print(f"Found {len(vehicle_cards)} vehicle entries. Starting extraction...")

    # 4. Loop through each container and extract specific data points
    for card in vehicle_cards:
        try:
            # Extract Vehicle Name (e.g., inside an <h3> tag)
            name_tag = card.find("span", class_="o-j4 o-jJ")
            name = name_tag.text.strip() if name_tag else "N/A"

            # Extract Price (e.g., inside a <span> tag)
            price_tag = card.find("span", class_="o-js o-j4 o-jJ")
            price = price_tag.text.strip() if price_tag else "N/A"

            # Extract an additional spec like Mileage if available
            launch_date_tag = card.find("div", class_="o-ei o-j1 o-jJ o-js")
            launch_date = launch_date_tag.text.strip() if launch_date_tag else "N/A"

            # Append the structured data to our list
            vehicle_data.append({
                "Model_Name": name,
                "Raw_Price": price,
                "launchdate": launch_date
            })

        except Exception as e:
            print(f"Skipping a card due to parsing error: {e}")
            continue

    return vehicle_data


def save_to_csv(data, filename="scraped_vehicles.csv"):
    if not data:
        print("No data to save.")
        return

    # Load into a Pandas DataFrame for easy manipulation and viewing
    df = pd.DataFrame(data)

    # Save to a clean CSV file
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Success! Data successfully saved to '{filename}'.")
    print("\nFirst 5 rows of your dataset:")
    print(df.head())


# --- Execution ---
if __name__ == "__main__":
    # Replace this with the specific URL or local HTML file path you want to test
    TARGET_URL = "https://www.carwale.com/upcoming-cars/"

    # Run the scraper
    extracted_data = scrape_automotive_data(TARGET_URL)

    # Export the results
    save_to_csv(extracted_data)
