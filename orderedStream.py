from typing import List
from collections import defaultdict
class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = defaultdict()
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        chunk = []
        if idKey not in self.stream:
            self.stream[idKey] = value
        
        if idKey == self.ptr:
            while self.ptr in self.stream:
                chunk.append(self.stream[self.ptr])
                self.ptr += 1
        return chunk


orderedstream = OrderedStream(5)
print(orderedstream.insert(3, "ccccc"))
print(orderedstream.insert(1, "aaaaa"))
print(orderedstream.insert(2, "bbbbb"))
print(orderedstream.insert(3, "eeeee"))
print(orderedstream.insert(4, "ddddd"))


