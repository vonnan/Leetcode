class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.lst = deque(encoding)
        self.size = sum(num for num in encoding[::2])
        

    def next(self, n: int) -> int:
        if n > self.size:
            self.size = 0
            return -1
        
        while n:
            f, num = self.lst.popleft(), self.lst.popleft()
            if f >= n:
                f -= n
                self.lst.appendleft(num)
                self.lst.appendleft(f)
                self.size -= n
                return num
            else:
                n -= f
                self.size -= f
            
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)