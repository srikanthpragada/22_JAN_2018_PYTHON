import json
import datetime

person = '{"name" : "Srikanth", "mobile" : "9059057000"}'

s = json.loads(person)
print( s["mobile"])

