
def  remove(list):
    print(id(list))
    for n in list:
        if n < 0:
            list.remove(n)
    print(list)



nums = [10,-20,20,-15]
print(id(nums))
remove(nums[:])
# remove(nums)

print(nums)