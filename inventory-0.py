# Inserting data into cars.db

import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    stock = [('1999', 'Ford_1', 6),
             ('2003', 'Ford_2', 11),
             ('2005', 'Ford_3', 7),
             ('2007', 'Honda_1', 12),
             ('2011', 'Honda_2', 32)
             ]

    c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", stock)
    
    
