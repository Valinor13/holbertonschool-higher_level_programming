#!/usr/bin/python3
"""A module containing commands to select from a database"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name " +
                   "FROM cities " +
                   "LEFT JOIN states " +
                   "ON cities.state_id = states.id " +
                   "ORDER BY cities.id ASC;")

    data = cursor.fetchall()

    for item in data:
        print(item)

    db.close()
