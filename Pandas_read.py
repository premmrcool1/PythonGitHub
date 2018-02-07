import pandas as pd
import csv
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='prem', passwd='prem', db='prem')

cur = conn.cursor()

with open('C:\Users\Premkumar.Nagarajan\Desktop\Learning\output_new.csv') as f:
   rows = csv.reader(f)
   next(rows)
   for r in rows:
       cur.execute(" INSERT INTO TBL_GOLD_COPY  VALUES (%s,%s,%s,%s,%s,%s) ", (r[3], r[4],r[6],r[7],r[8],r[9]))
    #cur.execute(" INSERT INTO TBL_GOLD_COPY1 VALUES (%s)",(r[1]))
       conn.commit()

conn.close()
