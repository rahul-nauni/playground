class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        return self._data.pop(0)
    
    def __len__(self):
        return len(self._data)
    
    def __max__(self):
        if len(self._data) == 0:
            return None
        return max(self._data)
    
    def __str__(self) -> str:
        return str(self._data)
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(4)
queue.enqueue(3)

print(queue.__str__())
print(f'max value: {queue.__max__()}')