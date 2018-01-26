
import random    # import random module

nums = []
for i in  range(1,11):
    nums.append(random.randint(100,200))

for n in nums:
    print(n)


squares = [ v * v for v in range(1,11) if v % 2 == 0 ]

print(squares)







