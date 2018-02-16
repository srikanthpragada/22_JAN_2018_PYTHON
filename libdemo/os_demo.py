import os

print("Current Directory : ",  os.getcwd())
print(r"Directories in : d:\python3")

# get list of files from the given path
for d in  os.listdir(r"d:\python3"):
    print(d)