from bisect import insort
from bisect import bisect_left
class SummaryRanges:

    def __init__(self):
        self.start = defaultdict(int)
        self.end = defaultdict(int)
        self.lst = []

    def addNum(self, val: int) -> None:
        
        if not self.lst:
            self.lst = [val]
            self.start[val] = val
            self.end[val] = val
        else:
            idx = bisect_left(self.lst, val)
            if idx == len(self.lst):
                self.lst.append(val)
                if val-1 in self.end:
                    s = self.end.pop(val -1)
                    self.start[s] = val
                    self.end[val] = s
                    
                else:
                    self.start[val] = val
                    self.end[val] = val
            else:
                if self.lst[idx] != val:
                    if val + 1 == self.lst[idx]:
                        e = self.start.pop(val + 1)
                        if idx != 0 and self.lst[idx -1] == val -1:
                            s = self.end.pop(val- 1)
                            self.start[s] = e
                            self.end[e] = s
                        else:
                            self.start[val] = e
                            self.end[e] = val
                    elif idx != 0 and self.lst[idx -1] == val -1:
                        s = self.end.pop(val- 1)
                        self.start[s] = val
                        self.end[val] = s
                    else:
                        self.start[val] = val
                        self.end[val] = val
                    self.lst.insert(idx, val)
                    
                        

    def getIntervals(self) -> List[List[int]]:
        return sorted([(s,e) for s,e in self.start.items()])
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()