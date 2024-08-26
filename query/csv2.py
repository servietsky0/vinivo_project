import sqlite3
import csv

conn = sqlite3.connect('data/vivino.db')
cursor = conn.cursor()

# avg wine price per country

cursor.execute("""
    SELECT countries.name, round(avg(vintages.price_euros)), vintages.ratings_average
    FROM vintages
    JOIN wines ON vintages.wine_id = wines.id
    JOIN regions ON wines.region_id = regions.id
    JOIN countries ON regions.country_code = countries.code
    GROUP BY countries.name
""")

rows = cursor.fetchall()

with open('data/second.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['country', 'priceAVG', 'rantingAVG']) 
    csvwriter.writerows(rows)  

conn.close()

import sqlite3
import csv

conn = sqlite3.connect('data/vivino.db')

# avg wine price per country

cursor.execute("""
    SELECT wines.name, vintages.price_euros, countries.name, wines.ratings_average
    FROM wines
    JOIN vintages ON wines.id = vintages.wine_id
    JOIN regions ON wines.region_id = regions.id
    JOIN countries ON regions.country_code = countries.code
""")

rows = cursor.fetchall()

with open('data/tiensconnard.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['wine', 'price', 'country', 'rating']) 
    csvwriter.writerows(rows)  

cursor = conn.cursor()

# vin prix pays ratingAVG