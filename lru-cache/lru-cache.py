from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key)
            
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dic and len(self.dic) == self.size:
            self.dic.popitem(last = False)
        self.dic[key] = value
        self.dic.move_to_end(key)
        

        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)