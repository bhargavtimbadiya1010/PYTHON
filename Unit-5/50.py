'''50.Write a program to retrieve database records
using fetch one, fetch many and fetch all methods.'''

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college"
)

cur = con.cursor()
cur.execute("SELECT * FROM students")

print("Fetch One:")
print(cur.fetchone())

print("\nFetch Many:")
print(cur.fetchmany(2))

print("\nFetch All:")
print(cur.fetchall())

con.close()

