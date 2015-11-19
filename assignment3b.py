# Assignment3b.py

import sqlite3
import random

with sqlite3.connect('newnum.db') as connection:
    c = connection.cursor()

    sql = {1: "SELECT avg(num) FROM numbers",
           2: "SELECT max(num) FROM numbers",
           3: "SELECT min(num) FROM numbers",
           4: "SELECT sum(num) FROM numbers"}

    prompt = """
    Select the operation you want to perform [1-5]:
    1. Average
    2. Max
    3. Min
    4. Sum
    5. Exit
    """

    while True:
        x = raw_input(prompt)
                
        if int(x) == 1:
            c.execute(sql[1])
            print c.fetchone()[0]
        elif int(x) == 2:
            c.execute(sql[2])
            print c.fetchone()[0]
        elif int(x) == 3:
            c.execute(sql[3])
            print c.fetchone()[0]
        elif int(x) == 4:
            c.execute(sql[4])
            print c.fetchone()[0]
        else:
            False

        
