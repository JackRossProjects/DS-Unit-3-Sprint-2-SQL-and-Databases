# /home/jack/Desktop/sprint/northwind.py

import sqlite3
import os

# Make connection and cursor for DB
DB_FILEPATH = os.path.join(os.path.dirname(__file__), '/home/jack/Desktop/northwind_small.sqlite3')
conn = sqlite3.connect(DB_FILEPATH)
curs = conn.cursor()

print("--- Sprint Part 2 Questions ---\n")

# P2Q1: What are the ten most expensive items in the database?
query = """
SELECT ProductName, UnitPrice AS "Price"
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""
result = curs.execute(query).fetchall()
print('P2Q1 Top ten most expensive products: ', result, '\n')

# P2Q2: What is the average age of an employee at time of hiring?
# Use SQL julianday function: https://www.w3resource.com/sqlite/sqlite-julianday.php
query = """
SELECT AVG(julianday(HireDate) - julianday(BirthDate)) / 365 AS "Average hire age"
FROM Employee
"""
result = curs.execute(query).fetchall()
print('P2Q2 Average age of employee at hiring: ', result, '\n')

# P2Q3: How does the average age of employee at hire vary by city?
query = """
SELECT City, AVG(julianday(HireDate) - julianday(BirthDate)) / 365 AS "Average hire age"
FROM Employee
GROUP BY City
"""
result = curs.execute(query).fetchall()
print('P2Q3 How does average age of employee at hire vary by city: ', result, '\n')


print("--- Sprint Part 3 Questions ---\n")

# P3Q1: What are the ten most expensive items (per unit price) in the database and their suppliers?
query = """
SELECT CompanyName, ProductName, UnitPrice AS "Price"
FROM Product
JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
"""
result = curs.execute(query).fetchall()
print('P3Q1 Top ten most expensive products AND their suppliers: ', result, '\n')

# P3Q2: What is the largest category (by number of unique products in it)?
query = """
SELECT CategoryName, COUNT(CategoryName) AS "Products"
FROM Product
JOIN Category
ON Product.CategoryId = Category.Id
GROUP BY CategoryName
ORDER BY Products DESC
LIMIT 1
"""
result = curs.execute(query).fetchall()
print('P3Q2 Largest category by unique product: ', result, '\n')

## P3Q3: Who's the employee with the most territories?
query = """
SELECT LastName, FirstName, COUNT(EmployeeId) AS "TerritoryId"
FROM Employee
JOIN EmployeeTerritory
ON Employee.Id = EmployeeTerritory.EmployeeId
GROUP BY EmployeeId
ORDER BY TerritoryId DESC
LIMIT 1
"""
result = curs.execute(query).fetchall()
print('P3Q3 Employee with most territories: ', result, '\n')


# Close connection to the database
curs.close()