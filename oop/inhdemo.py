
class Base:
    def print(self):
        print("In Base")

class Derived(Base):
    pass
    # def print(self):
    #     print("In Derived")

class Derived1(Base):
    pass
    # def print(self):
    #     print("In Derived")


class Derived2(Derived):
    pass
    # def print(self):
    #     print("In Derived2")


obj = Derived2()
obj.print()

print( Derived2.__mro__)
print( Derived1.__mro__)
print( Derived2.__bases__)

