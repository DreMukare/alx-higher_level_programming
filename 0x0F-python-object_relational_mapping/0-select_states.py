#!/usr/bin/python3
''' lists all states from the database hbtn_0e_0_usa '''

import MySQLdb

db = MySQLdb.connect(host='localhost', user='root', passwd='omoshiroi', port=3306, db='hbtn_0e_0_usa')
cur = db.cursor()
cur.execute('SELECT * FROM states ORDER BY id')
results = cur.fetchall()
for row in results:
    print(row)
db.close()
