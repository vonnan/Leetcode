from bisect import bisect
from bisect import insort

class MyCalendar:

    def __init__(self):
        self.date = []

    def book(self, start: int, end: int) -> bool:
        if not self.date:
            self.date.append((start, end))
            return True
        idx = bisect(self.date, (start, end))
        
        if idx == 0:
            if end > self.date[idx][0]:
                return False
        elif idx== len(self.date):
            if start < self.date[idx-1][1]:
                return False
        elif (end > self.date[idx][0]) or (start < self.date[idx-1][1]):
            return False
        
        self.date.insert(idx, (start, end))
        return True
            
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)