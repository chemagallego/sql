#JOINing data

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    # retrieve data
    for row in c.execute("""SELECT population.city, population.population,
            regions.region FROM population, regions
            WHERE population.city = regions.city"""):
        print row[0], row[1], row[2]

    
