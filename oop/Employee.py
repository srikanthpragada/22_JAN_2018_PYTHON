
class Employee:
    # Static attributes
    __hraper = 25
    __count = 0

    @staticmethod
    def sethraper(newper):
        Employee.__hraper = newper

    @staticmethod
    def getcount():
        return Employee.__count

    def __init__(self,name, salary):
        self.__name = name
        self.__salary = salary
        Employee.__count += 1

    def __del__(self):
        Employee.__count -= 1

    def get_salary(self):
        return self.__salary + self.__salary * Employee.__hraper / 100


e1 = Employee("Abc",50000)
e2 = Employee("Pqr",75000)
e3 = e1
print(Employee.getcount())
del  e2
print(Employee.getcount())





