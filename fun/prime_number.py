
# program to print whether a number is prime or not
# it takes input from command line arguments

import sys
import my_numbers

if  my_numbers.isprime( int(sys.argv[1])):
    print("Yes. Prime Number!")
else:
    print("No. Not a prime number")
