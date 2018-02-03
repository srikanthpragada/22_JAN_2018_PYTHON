

st = input("Enter a number :")
names = ['a','b','c']

try:
  v = intt(st)
  print("Value entered is ", v)
  print(names[v])
except(ValueError):
  print("Sorry! Invalid number!")
else:
  print("Success")
finally:
  print("Finally")

print("The End!")



