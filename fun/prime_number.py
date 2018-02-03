# program to print whether a number is prime or not
# it takes input from command line arguments

import sys
import my_numbers

if len(sys.argv) < 2:
   print('Sorry! Missing number');
   sys.exit(0)  # exit program

for i in range(1, len(sys.argv)):
    try:
        num  = int(sys.argv[i])
        if num < 0:
            raise Exception()

        if  my_numbers.isprime(num):
            print("{} is prime number!".format(num))
        else:
            print("{} is not a prime number".format(num))
    except ValueError:
        print("Sorry! Invalid input : ", sys.argv[i])
    except Exception:
        print("Sorry! Negative input not accepted!")

