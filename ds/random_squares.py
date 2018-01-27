import random

nums = {}

for n in range(1,11):
    n = random.randint(1,100)
    nums[n] = n * n

for v,s in nums.items():
    print("%3d %6d" % (v, s))


print("No. of entries ", len(nums))