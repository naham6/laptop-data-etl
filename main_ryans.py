
from config import R_URL, DB_NAME  
from extract.ryans_scraper import fetch_html, parse_laptops
from transform.cleaner import transform_r_data
from load.database import save_to_database 

def scrape_ryans():
    all_laptops = []
    page = 1
    
    while True:
        current_url = f"{R_URL}&page={page}"
        print(f"Loading Page {page}")
        
        raw_html = fetch_html(current_url)
        laptops_on_page = parse_laptops(raw_html)
        
        if not laptops_on_page:
            print(f"Reached the end")
            break
            
        all_laptops.extend(laptops_on_page)
        print(f"Found {len(laptops_on_page)} laptops. Total collected: {len(all_laptops)}")
        page = page + 1
        
        '''if page > 2:
            print("for testing.")
            break'''
            
    if all_laptops:
        df = transform_r_data(all_laptops)
        
        if df is not None:
            df.to_csv("ryans_laptops.csv", index=False)
            print("\nSaved csv'")
            save_to_database(df, DB_NAME, "ryans_inventory")

if __name__ == "__main__":
    scrape_ryans()