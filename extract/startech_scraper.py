from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def fetch_s_html(url):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")#keeping headless OFF
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(url)
        print("Waiting to load...")
        time.sleep(10) 
        return driver.page_source
    except Exception as e:
        print(f"Error fetching page: {e}")
        return None
    finally:
        driver.quit()

def parse_s_laptops(html):
    if not html:
        return []
        
    print("Parsing HTML...")
    soup = BeautifulSoup(html, "html.parser")
    laptops = []
    
    items = soup.find_all("div", class_="p-item")
    
    for item in items:
        try:
            name_tag = item.find("h4", class_="p-item-name").find("a")
            name = name_tag.get_text(strip=True)
            full_url = name_tag.get("href")
            
            price_tag = item.find("div", class_="p-item-price").find("span")
            raw_price = price_tag.get_text(strip=True)
            
            laptops.append({
                "store": "StarTech",
                "name": name,
                "price": raw_price,
                "full_url": full_url
            })
            
        except AttributeError:
            continue #skipping if the box misses anything
            
    return laptops