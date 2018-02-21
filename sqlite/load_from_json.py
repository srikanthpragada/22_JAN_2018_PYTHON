import json
import sqlite3

f = open("new_prices.json","rt")
json_data = json.load(f)

con = sqlite3.connect("e:\\classroom\\python\\jan22\\jan22.db")
cur = con.cursor()
try:
    for row in json_data:
        values = (row["price"], row["id"])
        cur.execute("update products set price = ? where id = ?", values)
        if cur.rowcount == 1:
            print("Updated Successfully!")
        else:  # Id not found
            values = (row["id"],row["name"],row["price"])
            cur.execute("insert into products values(?,?,?,0)", values)
            print("Inserted Successfully!")
    else:
        con.commit()  # At the end commit all changes

except Exception as ex:
    con.rollback()
    print("Sorry! Error -->", ex)
finally:
    con.close()


