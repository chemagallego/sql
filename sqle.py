# SELECT

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    # use for loop to iterate

    for row in c.execute("SELECT firstname, lastname FROM employees"):
        print row[0], row[1]
    
    
