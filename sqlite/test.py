
import sqlite3

con = sqlite3.connect("e:\\classroom\\python\\jan22\\jan22.db")
print(dir(con))

cur = con.cursor()
print(cur)




