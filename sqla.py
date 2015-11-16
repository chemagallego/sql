# import library
import sqlite3

# create a new DB
conn = sqlite3.connect('new.db')

# get a cursor object to execute sql
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)

# close DB connection
conn.close()
