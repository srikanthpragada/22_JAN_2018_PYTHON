import random


def nums():  # Generator
    for v in range(1, 11):
        yield random.randint(1, 100)


# Return unique numbers in the range 1 to 100
def unique_nums():  # Generator
    nums = set()
    while len(nums) < 10:
        num = random.randint(1, 100)
        if num not in nums:
            nums.add(num)
            yield num
        else:
            print(num, ' is duplicate')


def nums_count(count=10, start=1, end=100):  # Generator
    print("nums_count")
    for v in range(1, count + 1):
        yield random.randint(start, end)


# for n in nums_count(start=100, end=200):
#     print(n)


for n in unique_nums():
    print(n)
