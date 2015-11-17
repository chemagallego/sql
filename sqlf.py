# UPDATE & DELETE & WHERE

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    # updating
    c.execute("UPDATE population SET population = 9000000 WHERE city='New York City'")
    
    # search and delete
    c.execute("DELETE FROM population Where city='Boston'")

    print '\nUPDATED DATA:\n'

    for row in c.execute("SELECT * FROM population"):
        print row[0], row[1], row[2]

    
    
    
