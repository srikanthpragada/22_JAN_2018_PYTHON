# module with number related functions

import math

# print("my_numbers module is being loaded!")

def iseven(n):
    return n % 2 == 0


def isprime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
