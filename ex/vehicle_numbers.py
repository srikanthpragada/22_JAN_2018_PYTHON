# vnumbers.txt – has vehicle numbers. Print all valid vehicle numbers.
# 2 chars, followed by 1 or 2 digits, followed by 1 or 2 chars, followed by 1 to 4 digits.
# Print all of them in the order of the numbers.
import re

vnums = set()


def take_number(v):
    return int(re.findall('\d+$', v)[0])


try:
    with open('vnumbers.txt', 'r') as f:
        for vno in f.readlines():
            if re.match("^[A-Z]{2}[0-9]{1,2}[A-Z]{1,2}[0-9]{1,4}$", vno):
                vnums.add(vno.strip())

    # for vnum in sorted(vnums, key = lambda v:  int(re.findall('\d+$', v)[0])):
    for vnum in sorted(vnums, key=take_number):
        print(vnum)

except OSError as ex:
    print("Sorry! Error: ", ex)
