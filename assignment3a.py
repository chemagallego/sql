# Assignment3a.py: Inserting random data in sqlite
# Page: 79 Book nº2

import sqlite3
import random

with sqlite3.connect('newnum.db') as connection:
    c = connection.cursor()

    c.executescript("""
                    DROP TABLE if exists numbers;
                    CREATE TABLE numbers(num int);
                    """)
    
    for i in range(100):
        rand_number = random.randint(0,1000)
        c.execute("INSERT INTO numbers VALUES(?)", (rand_number,))
        #                                                     #,
        # Don't forget last "comma" to avoiding 'unsupported data type error'
        # It's necessary to complete the tuple
