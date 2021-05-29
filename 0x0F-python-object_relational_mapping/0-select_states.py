#!/usr/bin/python3
"""A module containing commands to select from a database"""


import MySQLdb
from sys import argv

db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC;")

data = cursor.fetchall()

for item in data:
    print(item)

db.close()
