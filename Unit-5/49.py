'''49.Write a program to connect Python with a
database and execute SQL queries. '''

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cur = con.cursor()

# Create database
cur.execute("CREATE DATABASE IF NOT EXISTS college")
cur.execute("USE college")
print("Database created")

# Create table
cur.execute("CREATE TABLE IF NOT EXISTS students (id INT, name VARCHAR(50), marks INT)")
print("Table created")

# Insert records
cur.execute("INSERT INTO students VALUES (1, 'Asha', 85)")
cur.execute("INSERT INTO students VALUES (2, 'Rahul', 90)")
cur.execute("INSERT INTO students VALUES (3, 'Neha', 78)")
cur.execute("INSERT INTO students VALUES (4, 'Yash', 80)")
cur.execute("INSERT INTO students VALUES (5, 'Kush', 92)")

con.commit()

# Display records
cur.execute("SELECT * FROM students")

for row in cur.fetchall():
    print(row)

con.close()
