

class Base1:
    def print(self):
        print("In Base1")

class Base2:
    def print(self):
        print("In Base2")

class Derived(Base2,Base1):
    def print(self):
        super().print()
        print("In Derived")


obj = Derived()
obj.print()
print(Derived.__mro__)

