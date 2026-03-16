import sqlite3
import pandas as pd
from config import DB_NAME

def analyze_laptops():
    print(f"Connecting to {DB_NAME}")
    
    try:
        conn = sqlite3.connect(DB_NAME)

        sql_command = """
        SELECT name, price
        FROM startech_inventory
        ORDER BY price DESC 
        LIMIT 5;
        """

        df = pd.read_sql_query(sql_command, conn)
        print(df)
        
    except Exception as e:
        print(f"DB error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    analyze_laptops()




'''    to make csvs,
    try:
        conn = sqlite3.connect(DB_NAME)
        df_ryans = pd.read_sql_query("SELECT * FROM ryans_inventory;", conn)
        df_ryans.to_csv("ryans.csv", index=False)
        

        print("Exporting StarTech inventory")
        df_startech = pd.read_sql_query("SELECT * FROM startech_inventory;", conn)
        df_startech.to_csv("startech.csv", index=False)
        
    except Exception as e:
        print(f"DB error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()'''






