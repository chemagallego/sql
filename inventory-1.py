# Updating 2 records using 'executescript method()'. Also output all records from the table.

import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    c.executescript("""
        UPDATE inventory SET Quantity = 17 WHERE Model ='Ford_3';
        UPDATE inventory SET Quantity = 17 WHERE Model ='Honda_1';
""")

    print '\nTABLE UPDATED:\n'

    for row in c.execute("SELECT * FROM inventory"):
        print row[0], row[1], row[2]
        
    print '\nSTOCK FOR Ford:\n'
    
    for row in c.execute("SELECT * FROM inventory WHERE Model LIKE 'Ford%'"):
        print row[0], row[1], row[2]
    
    
