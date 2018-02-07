class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 0 or age > 125:
            raise ValueError('Invalid age.')
        else:
            self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 125:
            raise ValueError('Invalid age.')
        else:
            self.__age = value


p = Person("Bill Gates", 62)
# print(p.get_age())
# print ( p.set_age(640))

p.age = 700
print(p.age)  # get value from property


