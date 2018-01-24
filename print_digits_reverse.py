# Prints digits in reverse order

num = int(input("Enter a number : "))
while num > 0:
    rem = num % 10 # get rightmost digit
    print(rem)
    num //= 10 # integer division
else:
    print("The end")

