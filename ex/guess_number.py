from random import randint

num = randint(1,25)
print(num)

for i in range(1,4):
    n = input("Enter your number :")
    if int(n) == num:
        print("You got it!")
        break
else:  # executes only when loop is terminated normally
    print("Sorry! Better luck next time.")