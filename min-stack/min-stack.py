from bisect import insort
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        insort(self.minstack, val)

    def pop(self) -> None:
        x = self.stack.pop()
        self.minstack.remove(x)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()