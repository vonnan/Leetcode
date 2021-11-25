class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.q = []

    def get(self, key: int) -> int:
        if key in self.dic:
            self.q.remove(key)
            self.q.append(key)
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.dic: 
            self.q.remove(key)
            self.q.append(key)
        else:
            self.q.append(key)
        if len(self.q) > self.capacity:
            self.dic.pop(self.q.pop(0))
        self.dic[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)