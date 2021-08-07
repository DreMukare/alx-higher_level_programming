#!/usr/bin/python3
'''
    lists all states with a name starting with N
    from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = db.cursor()
    query = 'SELECT * FROM states WHERE name LIKE {:s}\
    ORDER BY id ASC'.format(argv[4])
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    db.close()
