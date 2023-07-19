from collections import OrderedDict
class MyHashMap(object):

    def __init__(self):
        self.map = OrderedDict()

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.map:
            self.map.update({key: value})
        else:
            self.map[key] = value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.map.get(key, -1)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.map:
            self.map.pop(key)
    

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(3))
obj.put(2, 1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))