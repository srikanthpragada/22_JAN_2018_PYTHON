
try:
    with open('names.txt','r') as f:
        lineno = 1
        for line in f.readlines():
            print(lineno,line, end ='')
            lineno += 1
except:
    print("File not found!")


