
import sqlite3

con = sqlite3.connect("e:\\classroom\\python\\jan22\\jan22.db")
cur = con.cursor()
try:
    cur.execute("select * from products order by upper(name)")
    total = 0
    for row in cur.fetchall():
        print("%s  %10d %3d %10d" % (str(row[1]).ljust(30), row[2], row[3], row[2] * row[3]))
        total +=  row[2] * row[3]

    print("Total : %10d" % total)

except Exception as ex:
    print("Sorry! Error -->", ex)
finally:
    con.close()




