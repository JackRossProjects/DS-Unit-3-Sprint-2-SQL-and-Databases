# /home/jack/Desktop/sprint/demo_data.py

import sqlite3
import os

""" Part 1: open connection/cursor, create table, add data """
DB_FILEPATH = os.path.join(
    os.path.dirname(
        __file__), '/home/jack/Desktop/unit3sprint2/demo_data.sqlite3')

# Connection and cursor
conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()


# Create the demo table
query = """
CREATE TABLE IF NOT EXISTS demo (
  s varchar(1) NOT NULL,
  x Integer NOT NULL,
  y Integer NOT NULL);
"""
result = curs.execute(query).fetchall()

# Insert data into db
insertion_query = '''INSERT INTO demo (
    s, x, y)VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7)'''
result = curs.execute(insertion_query).fetchall()

# Commit insert so data will save
conn.commit()

print("Sprint Part 1 Questions")

# Number of rows in db (SHOULD BE 3)
query = """
SELECT COUNT(*) AS "Num of Rows"
FROM demo
"""
result = curs.execute(query).fetchall()
print('P1Q1 Rows: ', result, '\n')

# How many rows are there where both x and y are at least 5?
query = """
SELECT COUNT(*) AS "Rows"
FROM demo
WHERE x >= 5
AND y >= 5
"""
result = curs.execute(query).fetchall()
print('P1Q2: Rows where X & y >=5: ', result, '\n')

# How many unique values of y?
query = """
SELECT COUNT(DISTINCT y) AS "Unique y values"
FROM demo
"""
result = curs.execute(query).fetchall()
print('P1Q3 Rows with unique y value: ', result, '\n')

# Close connection
curs.close()
