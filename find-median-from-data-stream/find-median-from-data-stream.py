from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.SL = SortedList([])
        self.size = 0

    def addNum(self, num: int) -> None:
        self.SL.add(num)
        self.size += 1

    def findMedian(self) -> float:
        m = self.size//2
        if self.size %2:
            return self.SL[m]
        else:
            return (self.SL[m] + self.SL[m-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()