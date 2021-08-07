#!/usr/bin/python3
'''
takes in an arg and displays all values in the table
state where in db hbtn_0e_usa where name matches arg
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON\
    cities.state_id = states.id WHERE states.name LIKE %(state_name)s\
    ORDER BY cities.id ASC", {'state_name': argv[4]})
    res = cur.fetchall()
    i = 0
    while i < len(res):
        if i != (len(res) - 1):
            print(res[i][0], end=', ')
        else:
            print(res[i][0])
        i = i + 1
    db.close()
