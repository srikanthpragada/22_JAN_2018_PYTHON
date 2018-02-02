# Remove vowels from a given string

st = input("Enter a string : ")

vowels = ['a','e','i','o','u']
newst = ''

for ch in st:
    if ch not in vowels:
        newst += ch

print(newst)


