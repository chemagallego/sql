# importing library
import sqlite3

# connection
with sqlite3.connect('cars.db') as connection:
    # cursor
    c = connection.cursor()
    
    # Adding new table
    c.execute("""CREATE TABLE orders(Make TEXT, Model TEXT, Order_date DATE)""")

    # New records for new table. Date format YYYY-MM-DD
    records_to_add = [
                    ('Ford', 'Ford_1', '2015-Nov-02'),
                    ('Ford', 'Ford_1', '2015-Nov-03'),
                    ('Ford', 'Ford_1', '2015-Nov-04'),
                    ('Ford', 'Ford_2', '2015-Nov-05'),
                    ('Ford', 'Ford_2', '2015-Nov-06'),
                    ('Ford', 'Ford_2', '2015-Nov-07'),
                    ('Ford', 'Ford_3', '2015-Nov-08'),
                    ('Ford', 'Ford_3', '2015-Nov-09'),
                    ('Ford', 'Ford_3', '2015-Nov-10'),
                    ('Honda', 'Honda_1', '2015-Nov-01'),
                    ('Honda', 'Honda_1', '2015-Nov-03'),
                    ('Honda', 'Honda_1', '2015-Nov-05'),
                    ('Honda', 'Honda_2', '2015-Nov-07'),
                    ('Honda', 'Honda_2', '2015-Nov-09'),
                    ('Honda', 'Honda_2', '2015-Nov-11')
                    ]

    # Adding new records
    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", records_to_add)

    # Output. My way :)
    for row in c.execute("""SELECT inventory.Make, inventory.Model,
            inventory.Quantity, orders.Order_date FROM inventory, orders
            WHERE inventory.Make = orders.Make
            ORDER by inventory.Model ASC"""):
    
    # As seen at https://github.com/realpython/book2-exercises/blob/master/sql/hw-sqlf.py
    # But "Inner Join" wasn't explained in the book, so I didn't use it. Anyway, INNER JOIN is a must.
    #
    #for row in c.execute("""SELECT inventory.Make, inventory.Model,
    #        inventory.Quantity, orders.Order_date FROM inventory INNER JOIN orders ON
    #        inventory.Make = orders.Make"""):        
        
        print "Make: " + row[0], "Model: " + row[1]
        print "Qty: " + str(row[2])
        print "Order Date: " + row[3]
        print 
