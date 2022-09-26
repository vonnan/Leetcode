class MyCircularQueue:

    def __init__(self, k: int):
        self.q = deque([])
        self.size = k

    def enQueue(self, value: int) -> bool:
        if len(self.q) == self.size:
            return False
        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        if not self.q:
            return False
        self.q.popleft()
        return True

    def Front(self) -> int:
        if not self.q:
            return -1
        return self.q[0]

    def Rear(self) -> int:
        if not self.q:
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return not self.q

    def isFull(self) -> bool:
        return len(self.q) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()