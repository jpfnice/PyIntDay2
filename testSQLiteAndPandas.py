import sqlite3
import pandas as pd

try:
    conn=sqlite3.connect(r"pyInt.db")
    df=pd.read_sql("SELECT * FROM product", conn)
    # read_csv, read_json, ....
    print(df)
    
    conn.close()
except Exception as ex:
    print(ex)
