class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.nxt = 0

    def next(self) -> int:
        
        if not self.v1:
            self.nxt = 1
        if not self.v2:
            self.nxt = 0
        if self.nxt == 0:
            self.nxt = 1- self.nxt
            return self.v1.pop(0)
        else:
            self.nxt = 1- self.nxt
            return self.v2.pop(0)

    def hasNext(self) -> bool:
        if not self.v1 and not self.v2:
            return False
        else:
            return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())