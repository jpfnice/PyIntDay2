"""
To create the table temperatures (if it already exists, 
                                  it gonna first be dropped)

"""
import sqlite3

try:

    with sqlite3.connect("epfl_2025.db") as conn:
        cursor=conn.cursor()
        cursor.execute("drop table if exists temperatures")
        cursor.execute("create table temperatures (city varchar(20), time time, date date, temp float)")
        cursor.close()

except Exception as ex:
    print(ex)