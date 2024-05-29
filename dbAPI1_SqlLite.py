
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

	                                     
                                                      
"""

import sqlite3 # compliant with the DBAPI 2

try:
    # Step 1: connection
    conn=sqlite3.connect(r"pyInt.db") # login + password + hostname if needed
    # Step 2: create a cursor object
    cursor=conn.cursor()
    # Step 3: using the cursor, execute SQL statements:
    #cursor.execute("create table product (name varchar(20) primary key, price float, qty int)")
    cursor.execute("insert into product values ('DELL 78', 56778.8, 2)")
    cursor.execute("insert into product values ('DELL 76', 2000.6, 10)")
    cursor.execute("insert into product values ('HP 10', 1000.6, 9)")
    # # print(f"{cursor.rowcount} rows were returned")
    cursor.execute("commit") 
    
    #cursor.execute("select * from product")
    # a "resultset" is returned
#     while True:
#         row = cursor.fetchone()
#         if row == None:
#             break
# #        print("{}, {}, {}".format(row[0], row[1], row[2]))
#         print(row)
    # res=cursor.fetchall()    
    # print(res)
#    print("{} rows were returned".format(cursor.rowcount))
      
    cursor.close()
    conn.close()
except Exception as ex:
    print(ex)