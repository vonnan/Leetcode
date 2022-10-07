from bisect import insort

class MyCalendarThree:

    def __init__(self):
       
        self.lst = []
        self.max_ = 0
        

    def book(self, start: int, end: int) -> int:
        
        insort(self.lst, (start, 1))
        insort(self.lst, (end, -1))
        ans = [val for _, val in self.lst]
        presum = accumulate(ans)
        return max(presum)
        
        
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)