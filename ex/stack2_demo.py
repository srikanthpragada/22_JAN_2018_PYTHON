class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("Stack is empty!")

# Stack that supports only one type of objects
class Stack:
    def __init__(self):
        self.data = []
        self.typ = None

    def push(self, value):
        if self.typ is None:  # first element
            self.typ = type(value)  # store type in typ

        if isinstance(value,self.typ):
            self.data.append(value)
        else:
            raise ValueError('Not a valid value : ' + str(value))


    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            raise EmptyStackError()

    @property
    def length(self):
        return len(self.data)


s = Stack()
s.push(10)
s.push(20)

s = Stack()
s.push("Abc")
s.push(10)



