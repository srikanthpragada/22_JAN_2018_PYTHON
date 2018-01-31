def isodd(n):
    return n % 2 == 1


nums = [12, 22, 19, 77, 80, 55]

onums = filter(isodd, nums)

for n in onums:
    print(n)

enums = filter(lambda n: n % 2 == 0, nums)

for n in enums:
    print(n)
