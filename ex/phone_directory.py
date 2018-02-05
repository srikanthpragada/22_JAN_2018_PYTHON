directory = {}

while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break

    number = input ("Enter phone number :")
    if name in directory:
        directory[name].add(number)
    else:
        directory[name] = set()
        directory[name].add(number)

for name,numbers in sorted(directory.items()):
    print(name, end = ' ')
    for num in sorted(numbers):
        print(' ', num, end=' ')

    print()   # next line
