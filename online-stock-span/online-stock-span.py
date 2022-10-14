class StockSpanner:

    def __init__(self):
        self.stack = [(inf, 0)]
        self.day = 0

    def next(self, price: int) -> int:
        
        self.day += 1
        
        while self.stack[-1][0] <= price:
            self.stack.pop()
        
        date = self.stack[-1][1]
        self.stack.append((price, self.day))
        return self.day - date


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)