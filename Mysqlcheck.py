#!/usr/bin/env python
from __future__ import print_function

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='prem', passwd='prem', db='prem')

cur = conn.cursor()

cur.execute("SELECT * FROM TBL_GOLD_COPY")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()