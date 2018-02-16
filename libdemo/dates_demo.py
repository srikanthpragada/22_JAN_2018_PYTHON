
from datetime import date, datetime, timedelta

t = timedelta(days=10)
print(t)
d = date.today() + t
print(d)
cd = date.today()
print( d > cd)

print(d.year, d.month, d.day)


