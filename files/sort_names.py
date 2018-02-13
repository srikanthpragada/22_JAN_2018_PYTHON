
try:
    with open('names.txt','r') as f:
        lines = set()
        for line in f.readlines():
            lines.add(line)

        for line in  sorted(lines):
            print(line, end='')
except:
    print("File not found!")


