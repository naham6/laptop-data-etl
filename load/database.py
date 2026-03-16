
import sqlite3
import pandas as pd

def save_to_database(df, db_name, table_name):#table_name for separate tables
    if df is None or df.empty:
        print("No data")
        return

    print(f"Saving {len(df)} records to table {table_name}")
    
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        
        print(f"Data saved to the {table_name}")
        
    except Exception as e:
        print(f"DB error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()