class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            raise ValueError("Stack is empty!")

    def __iter__(self):
       self.pos = len(self.data) - 1
       return self

    def __next__(self):
      if self.pos < 0:
         raise StopIteration()
      else:
         value = self.data[self.pos]
         self.pos -= 1
         return value

    @property
    def length(self):
        return len(self.data)


s = Stack()
s.push(10)
s.push(20)
s.push(30)

for v in s:
    print(v)

