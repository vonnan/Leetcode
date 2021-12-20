class MRUQueue:

    def __init__(self, n: int):
        self.stack = list(range(1, n+1))

    def fetch(self, k: int) -> int:
        self.stack = self.stack[:k-1] + self.stack[k:] + [self.stack[k-1]]
        return self.stack[-1]


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)