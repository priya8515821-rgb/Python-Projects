import requests
from bs4 import BeautifulSoup
import csv

# Target URL
url = 'https://news.google.com'

def run_scraper():
    print(f"Connecting to {url}...")
    try:
        response = requests.get(url)
        # Check if connection is successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Finding headlines (h3 tags)
            headlines = soup.find_all('h3')
            
            # --- THIS PART PRINTS THE HEADLINES ---
            print(f"Success! Found {len(headlines)} headlines.")
            print("\nRecent Headlines:")
            for i, head in enumerate(headlines[:5]):
                print(f"{i+1}. {head.text}")
            # --------------------------------------

        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_scraper()
