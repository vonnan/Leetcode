class MapSum:

    def __init__(self):
        self.dic= defaultdict(int)
        self.pre = defaultdict(set)

    def insert(self, key: str, val: int) -> None:
        self.dic[key] = val
        prefix = ""
        for c in key:
            prefix += c
            self.pre[prefix].add(key)
            
    def sum(self, prefix: str) -> int:
        res = sum(self.dic[word] for word in self.pre[prefix])
        return res
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)