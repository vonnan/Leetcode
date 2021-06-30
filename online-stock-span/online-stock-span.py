class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        res = self.day - self.stack[-1][1] if self.stack else self.day
        self.stack.append((price, self.day))
        
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)