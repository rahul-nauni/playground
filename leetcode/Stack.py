class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self.is_empty():
            return self._data.pop()

    def __len__(self):
        return len(self._data)
    
    def __max__(self):
        if self.is_empty():
            return None
        return max(self._data)
    
    def is_empty(self):
        return len(self._data) == 0

stack = Stack()
#stack.push(1)
#stack.push(2)
#stack.push(3)

#print(stack.pop())
#print(f'max value: {stack.__max__()}')

x = 123
for i in str(x):
    if stack.pop() != i:
        stack.push(i)

