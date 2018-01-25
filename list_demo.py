
nums = [102,33,11,23,30,98,90,15,883]

enums = []
onums = []

for n in nums:
    if n % 2 == 0:
        enums.append(n)
    else:
        onums.append(n)

print(enums)
print(onums)

# squares = []
#
# for n in nums:
#     squares.append(n * n)
#
# print(squares)

sqrs = [ n * n for n in nums ]
print(sqrs)
