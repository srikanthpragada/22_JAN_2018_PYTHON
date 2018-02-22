
import cx_Oracle
import os

os.environ["PATH"] = r"d:\python3\instantclient_12_2"
con = cx_Oracle.connect("hr/hr@localhost/xe")

cur = con.cursor()
try:
    row = (4,'Samsung Note 8',56000,5)
    cur.execute("insert into products values({},'{}',{},{})".format(row[0],row[1],row[2],row[3]));
    print("Row Count : " , cur.rowcount)
    con.commit()

except Exception as ex:
    con.rollback()
    print("Sorry! Error -->", ex)
finally:
    pass
    #con.close()




