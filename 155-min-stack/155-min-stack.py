from bisect import insort
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        insort(self.min_, val)

    def pop(self) -> None:
        num = self.stack.pop()
        self.min_.remove(num)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()