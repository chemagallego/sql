# Homework: SQLite Functions
# Pags: 77-78 Book nº2

import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()


    sql = {'Ford_1 count'    : "SELECT count(Make) FROM orders WHERE Model = 'Ford_1'",
            'Ford_2 count'   : "SELECT count(Make) FROM orders WHERE Model = 'Ford_2'",
            'Ford_3 count'  : "SELECT count(Make) FROM orders WHERE Model = 'Ford_3'",
            'Honda_1 count'  : "SELECT count(Make) FROM orders WHERE Model = 'Honda_1'",
            'Honda_2 count' : "SELECT count(Make) FROM orders WHERE Model = 'Honda_1'"}


    for k, v in sql.iteritems():
        c.execute(v)

        result = c.fetchone()

        print k + ":", result[0]
        print


    for row in c.execute("""SELECT inventory.Make, inventory.Model,
            inventory.Quantity, orders.Order_date FROM inventory INNER JOIN orders
            ON inventory.Model = orders.Model"""):

        print row[0], row[1]
        print row[2]
        print row[3]
        print
