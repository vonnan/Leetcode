from bisect import bisect_left
from bisect import bisect

class RangeModule:

    def __init__(self):
        self.range = []

    def addRange(self, left: int, right: int) -> None:
        idx_lo = bisect_left(self.range, left)
        idx_hi = bisect(self.range, right)
        if idx_lo %2 : 
            idx_lo -= 1
            left = self.range[idx_lo]
        if idx_hi % 2:
            right = self.range[idx_hi]
            idx_hi += 1
        
        self.range = self.range[:idx_lo] + [left, right] + self.range[idx_hi:]
            

    def queryRange(self, left: int, right: int) -> bool:
        idx_lo = bisect(self.range, left)
        return idx_lo %2 and idx_lo < len(self.range) and self.range[idx_lo -1] <= left < right <= self.range[idx_lo]

    def removeRange(self, left: int, right: int) -> None:
        idx_lo = bisect_left(self.range, left)
        idx_hi = bisect(self.range, right)
        
        new = []
        if idx_lo % 2:
            
            new += [left]
            
        if idx_hi %2:
            new += [right]
            
        self.range = self.range[:idx_lo] + new +self.range[idx_hi:]
            
            
            
            
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)