import cx_Oracle
import os



# Change system path
os.environ["PATH"] = r"d:\python3\instantclient_12_2"
con = cx_Oracle.connect("hr/hr@localhost/xe")
print("Connected to Oracle")
con.close()

