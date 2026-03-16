import pandas as pd

def transform_r_data(raw_data):
    if not raw_data: return None
    
    print("Transforming data")
    df = pd.DataFrame(raw_data)
    df['full_url'] = "https://www.ryans.com/" + df['product_slug']
    df = df.drop(columns=['product_slug'])
    
    df['price'] = pd.to_numeric(df['price'])
    return df

def transform_s_data(raw_data):
    if not raw_data: return None
    
    print("Transforming data")
    df = pd.DataFrame(raw_data)
    
    df['price'] = df['price'].str.replace('৳', '', regex=False)
    df['price'] = df['price'].str.replace(',', '', regex=False)
    
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0).astype(int)#outofstock/TBA filled with 0
    
    return df