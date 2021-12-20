"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        stack = []
        for x in schedule:
            for interval in x:
                stack.append((interval.start, interval.end))
        stack.sort() 
        
        res = []
        start, end = stack.pop(0)
        while stack:
            s,e = stack.pop(0)
            if s > end:
                res.append((start, end))
                start, end = s, e
            else:
                end = max(end, e)
        
        res.append((start, end))
        
        ans = []
        
        for a,b in zip(res, res[1:]):
            
            ans.append(Interval(a[1], b[0]))
        
        return ans