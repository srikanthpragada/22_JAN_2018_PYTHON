
import sqlite3

con = sqlite3.connect("e:\\classroom\\python\\jan22\\jan22.db")
cur = con.cursor()
try:
    id = input("Product Id : ")
    row = (id,)
    cur.execute("delete from products where id = ?", row)
    if cur.rowcount == 1:
        print("Deleted successfully!")
        con.commit()
    else:
        print("Product Id Not Found!")

except Exception as ex:
    con.rollback()
    print("Sorry! Error -->", ex)
finally:
    con.close()




