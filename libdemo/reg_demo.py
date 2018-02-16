
import re


m1 = re.search("([\w]+) (\d+) (\d+)","Programmer 5000 50000 3 years of exp.")

print( m1.group(0))

print( m1.group(1))
print( m1.group(2))
print( m1.group(3))

for g in m1.groups():
    print(g)





