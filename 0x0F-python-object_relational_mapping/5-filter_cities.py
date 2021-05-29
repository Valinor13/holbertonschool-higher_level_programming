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

    cities = ""
    for i in range(len(data)):
        if argv[4] == data[i][2]:
            cities += data[i][1] + ", "
    print(cities[:-2])
    db.close()
