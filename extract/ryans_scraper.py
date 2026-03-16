
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def fetch_html(url):
    chrome_options = Options()
    
    chrome_options.add_argument("--window-size=1920,1080")#headless blocked
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(url)
        print("Waiting to load")
        time.sleep(10) 
        return driver.page_source
    except Exception as e:
        print(f"Error fetching page: {e}")
        return None
    finally:
        driver.quit()

def parse_laptops(html):
    if not html:
        return []
        
    print("looking for JSON data")
    soup = BeautifulSoup(html, "html.parser")
    laptops = []
    buttons = soup.find_all("button", class_="product-preview-btn")#targetting the specific buttons that hold the JSON payload
    
    for btn in buttons:
        json_string = btn.get("data-item")
        
        if not json_string:
            continue
            
        try:
            data = json.loads(json_string)
            #slug = data.get("product_slug")
            laptops.append({
                "store": "Ryans",
                "product_id": data.get("product_id"),
                "name": data.get("product_name"),
                "price": data.get("product_price2"), 
                "product_slug": data.get("product_slug")
            })

            
        except json.JSONDecodeError:
            print("malformed JSON string,skipping")
            continue
            
    unique_laptops = {laptop['product_id']: laptop for laptop in laptops}.values()#removing duplicate laptops based on their unique ID
    
    return list(unique_laptops)