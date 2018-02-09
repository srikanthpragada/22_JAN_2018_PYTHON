class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("Stack is empty!")


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

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
s.push("abc")

print(s.length)
print(s.pop())
print(s.pop())

ss = Stack()
ss.push("Abc")
ss.push("Bbc")
print(ss.pop())

