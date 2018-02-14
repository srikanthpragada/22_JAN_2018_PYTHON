
try:
    with open('names.txt','r') as f:
        lines = set()
        for line in f.readlines():
            lines.add(line.strip('\n'))

        for line in  sorted(lines):
            print(line)
except:
    print("File not found!")


