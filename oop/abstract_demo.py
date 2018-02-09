from abc import ABC,abstractmethod

class Base(ABC):
    @abstractmethod
    def process(self):
        print("I am in abstract method")  # Abstract method can have code
        pass


class Derived(Base):
    def process(self):
        super().process()
        pass

d = Derived()
d.process()
# b = Base()


