
"""
SQL: select, insert, update, delete, create, drop, ....

Database API: Sqlite, SQL*Server, MySQL, MariaDB, postgreSQL, Oracle, ...


1) Connection: hostname, port number, login name/password
2) creation of Python object that will encapsulate SQL statement
3) execution of the Python object
4) analyse the value returned by the database engine (a number, a resultset, 
                                                      an exception)
5) Close the connection
        
Examples of SQL statements:
CREATE TABLE product (
    name  STRING PRIMARY KEY,
    price REAL,
    qty   INT
);

DROP TABLE product;

INSERT INTO product (
                        name,
                        price,
                        qty
                    )
                    VALUES (
                        'product1',
                        3.24,
                        12
                    );
					
INSERT INTO product VALUES (
                        'product1',
                        3.24,
                        12
                    );
					
SELECT name,price,qty FROM product; # <=> select * from product

SELECT name,
       price,
       qty,
       qty*price
  FROM product;
 
SELECT *  FROM product WHERE qty > 10;

UPDATE product
   SET price = price * 1.1
 WHERE name = 'Prod1';
 
DELETE FROM product
      WHERE qty = 0;

	                                     
COMMIT      # validate a transaction (the insert,delete,update done previously)                                                      

ROLLBACK    # invalidate the transaction (the insert,delete,update done previously)                                                      
"""

import sqlite3 # compliant with the DBAPI 2

# Step 1: connection
with sqlite3.connect(r"pyInt.db") as conn: # login + password + hostname if needed
    try:
        # Step 2: create a cursor object
        cursor=conn.cursor()
        # Step 3: using the cursor, execute SQL statements:
        cursor.execute("update product set price=100.5 where name='HP 10'")
        print(f"Row count is {cursor.rowcount} ")
        cursor.execute("commit") 
        cursor.execute("select name, price, qty, qty*price from product")
         
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            print(f"{row[0]:12s} -> {row[1]}, {row[2]}, {row[3]}")
        cursor.close()

    except Exception as ex:
        print(ex)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    