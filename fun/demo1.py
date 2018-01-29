def two():
    return (10,20)

def add(n1, n2):
    return n1 + n2

def mul(n1=10, n2=10):
    return n1 * n2


print(add(10, 20))
print(add(n2=100, n1=200))
print(add("Abc", "Xyz"))

print(mul(10, 20))
print(mul(10))
print(mul())
print(mul(n2=5))

f,s = two()

print(f,s)

