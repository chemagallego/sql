#JOINing data

import sqlite3

with sqlite3.connect('new.db') as connection:
    c = connection.cursor()

    # retrieve data ORDER by population
    for row in c.execute("""SELECT DISTINCT population.city, population.population,
            regions.region FROM population, regions
            WHERE population.city = regions.city
            ORDER by population.population ASC"""):
        
        print "City: " + row[0]
        print "Population: " + str(row[1])
        print "Region: " + row[2]
        print

    
