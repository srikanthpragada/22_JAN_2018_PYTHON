
import sqlite3

con = sqlite3.connect("e:\\classroom\\python\\jan22\\jan22.db")
cur = con.cursor()
try:
    row = (7,'Samsung Note 8',56000,5)
    cur.execute("insert into products values(?,?,?,?)", row)
    print("Row Count : " , cur.rowcount)
    con.commit()
except Exception as ex:
    con.rollback()
    print("Sorry! Error -->", ex)
finally:
    con.close()




