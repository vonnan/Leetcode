from bisect import bisect
from bisect import insort

class MyCalendar:

    def __init__(self):
        self.lst = [[-inf, -inf], [inf, inf]]

    def book(self, start: int, end: int) -> bool:
       
        idx = bisect(self.lst, [start, end])
        if start < self.lst[idx -1][1] or end > self.lst[idx][0]:
            return False
        else:
            self.lst.insert(idx, [start, end])
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)