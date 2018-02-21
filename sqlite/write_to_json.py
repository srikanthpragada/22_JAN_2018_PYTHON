import json
import sqlite3


def tuple_to_dict(row):
    row_dict = {"id": row[0], "name": row[1], "price": row[2], "qty": row[3]};
    return row_dict


f = open("products.json", "wt")

con = sqlite3.connect("e:\\classroom\\python\\jan22\\jan22.db")
cur = con.cursor()
products = []
try:
    cur.execute("select * from products")
    for row in cur.fetchall():
        product = tuple_to_dict(row)  # convert tuple to dictionary
        products.append(product)      # add dictionary to list

    # write list of products to json
    json.dump(products, f)
    print("Wrote products to Json")
    f.close()
except Exception as ex:
    print("Sorry! Error -->", ex)
finally:
    con.close()
