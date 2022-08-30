class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.q = deque([])
        self.dic = defaultdict(int)

    def get(self, key: int) -> int:
        if key in self.dic:
            self.q.remove(key)
            self.q.append(key)
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            
            self.q.remove(key)
            
        else:
            
            if len(self.q) == self.cap:
                self.dic.pop(self.q.popleft())
        self.dic[key] = value
        self.q.append(key)

                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)