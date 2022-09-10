class FrontMiddleBackQueue:

    def __init__(self):
        self.q = []

    def pushFront(self, val: int) -> None:
        self.q.insert(0, val)
        

    def pushMiddle(self, val: int) -> None:
        n = len(self.q)
        self.q.insert(n//2, val)
        
    def pushBack(self, val: int) -> None:
        self.q.append(val)
        

    def popFront(self) -> int:
        if self.q:
            return self.q.pop(0)
        else:
            return -1

    def popMiddle(self) -> int:
        n = len(self.q)
        
        if n:
            return self.q.pop((n-1)//2)
        else:
            return -1

    def popBack(self) -> int:
        if self.q:
            return self.q.pop()
        else:
            return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()