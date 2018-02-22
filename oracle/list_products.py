
import cx_Oracle
import os

os.environ["PATH"] = r"d:\python3\instantclient_12_2"
con = cx_Oracle.connect("hr/hr@localhost/xe")
cur = con.cursor()
try:
    cur.execute("select * from products order by upper(pname)")
    total = 0
    for row in cur.fetchall():
        print("%s  %10d %3d %10d" % (str(row[1]).ljust(30), row[2], row[3], row[2] * row[3]))
        total +=  row[2] * row[3]

    print("Total : %10d" % total)
except Exception as ex:
    print("Sorry! Error -->", ex)
finally:
    pass
   # con.close()




