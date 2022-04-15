class MyCalendarTwo:

    def __init__(self):
        self.dic = defaultdict(int)
        

    def book(self, start: int, end: int) -> bool:
        self.dic[start] += 1
        self.dic[end] -=1
        tot = 0
        
        for key in sorted(self.dic):
            tot += self.dic[key]
            if tot >= 3:
                self.dic[start] -= 1
                self.dic[end] += 1
                return False
            if key > end:
                break
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)