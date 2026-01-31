import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl # Library needed for pandas to write Excel files

# Target URL for a simple stock index page (e.g., Yahoo Finance general index)
URL = "https://finance.yahoo.com"

def scrape_stock_indices(url):
    print(f"Connecting to {url} to fetch world indices...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"Failed to fetch page. Status code: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        data = []

        # Find the main table containing the data (Yahoo uses specific classes)
        table = soup.find('table')
        if table:
            # We are selecting all table rows
            rows = table.find_all('tr', class_='data-row')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) > 5: # Ensure we have enough columns
                    # Extract data from specific column indices
                    data.append({
                        'Symbol': cols[0].text.strip(),
                        'Name': cols[1].text.strip(),
                        'Price': cols[2].text.strip(),
                        'Change': cols[3].text.strip(),
                        'Percent Change': cols[4].text.strip()
                    })

        # Use Pandas to create a clean spreadsheet
        df = pd.DataFrame(data)
        output_filename = "World_Stock_Indices.xlsx"
        df.to_excel(output_filename, index=False, engine='openpyxl')
        
        print(f"\nSuccess! Saved {len(data)} indices to {output_filename}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the web request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    scrape_stock_indices(URL)
