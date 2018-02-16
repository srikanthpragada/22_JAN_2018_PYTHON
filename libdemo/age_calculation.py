from datetime import *

dobs = "24-10-1998"
dob  = datetime.strptime(dobs,"%d-%m-%Y")  # string to datetime
today = datetime.today()

period = today - dob     # Get timedelta between two dates
print( period.days // 365)
