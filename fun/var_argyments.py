
def sum(*nums, message="Total"):
    total=0
    for n in nums:
        total += n

    print(message,total)


sum(10, 20, 30)
sum(10, 20, 30, message = "Sum")

print(10,20,30, end='*', sep='-')

