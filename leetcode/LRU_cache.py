# Definition for doubly-linked list
# Each node will point to previous and next node in list, as well as a key and value
class ListNode():
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return f"ListNode({self.key}, {self.val})"

class LRUCache():
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # capacity of cache
        self.capacity = capacity
        
        # head and tail
        self.head = ListNode() # LRU
        self.tail = ListNode() # MRU
        
        # connect head and tail
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # key -> node
        self.cache = {}
    
    # Helper functions to maintain order of cache
    # add node to front of list
    def _insert(self, node):
        # | prev | <--> | next |
        # | prev | <--> | node | <--> | next |
        next = self.head.next
        self.head.next = node
        next.prev = node
        node.next = next
        node.prev = self.head

    # delete node from list
    def _remove(self, node):
        # | prev | <--> | node | <--> | next |
        # | prev | <--> | next |
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # get key from cache in O(1) time
    def get(self, key) -> int:
        """
        :type key: int
        :rtype: int
        """
        # check if key in cache, else return -1
        if key in self.cache:
            # move node to front of list
            node = self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1
    
    # update cache in O(1) time
    def put(self, key, value) -> None:
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if key in cache, udate value and move node to front
        if key in self.cache:
            node = self.cache[key]
            node.val = value # update value
            self._remove(node)
            self._insert(node)
        else:
            # add new node to cache
            node = ListNode(key, value)
            self.cache[key] = node
            self._insert(node)
            if len(self.cache) > self.capacity:
                # remove LRU node from cache
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 1)
print(obj.get(1)) 
obj.put(2, 2)
print(obj.get(2))
obj.put(3, 3)
obj.put(4, 4)
print(obj.get(2))