class Base:
    def print(self):
        print("In Base")


class Base1(Base):
    pass
    # def print(self):
    #     print("In Base1")


class Base2(Base):
    def print(self):
        print("In Base2")


class Derived(Base1, Base2):
    pass
    # def print(self):
    #     super().print()
    #     print("In Derived")


obj = Derived()
obj.print()
print(Derived.__mro__)
