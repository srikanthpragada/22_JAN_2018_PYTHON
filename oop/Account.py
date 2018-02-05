class Account:
    def __init__(self, acno, holder, balance=0):
        # instance variables or attributes
        self.__acno = acno
        self.__holder = holder
        self.__balance = balance

    # Methods
    def print(self):
        print(self.__acno)
        print(self.__holder)
        print(self.__balance)

    def deposit(self,amount):
        self.__balance += amount


a1 = Account(1,"Mr. James",10000) # object
a1.print()
a1.deposit(5000)

a2 = Account(2,"Mr. Bill")
a2.print()
a4 = Account(1,"Mr. James",10000)
a3 = a1
print(a1 == a3)
print(a1 == a2)
print(a1 == a4)

print(a1)







