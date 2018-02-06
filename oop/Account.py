class Account:
    def __init__(self, acno, holder, balance=0):
        # instance variables or attributes
        self.__acno = acno
        self.__holder = holder
        self.__balance = balance

    def __str__(self):
        return "%d %s %f" % (self.__acno, self.__holder, self.__balance)

    # overloads == operator
    def __eq__(self, other):
       # print(self,other)
       return  self.__acno == other.__acno

    # overloads > operator
    def __gt__(self, other):
       return self.__balance > other.__balance

    #  Supports + i.e.  a3 = a1 + a2
    def __add__(self, other):
        return Account(self.__acno, self.__holder, self.__balance + other.__balance)

    def __del__(self):
        print("Object is being destoryed!")

    # Methods
    def print(self):
        print(self.__acno)
        print(self.__holder)
        print(self.__balance)

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount;
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance


a1 = Account(1,"Mr. James",10000) # object
# a1._Account__balance = 1000  # Access private member
a1.deposit(5000)
a4 = Account(1,"Mr. James",10000)
print(a1 + a4)











