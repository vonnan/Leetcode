from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        start = sorted([(intervals[i][0], i) for i in range(n)])
        
        res = []
        
        for i, lst in enumerate(intervals):
            _, end = lst
            idx = bisect_left(start, (end, -1))
            if idx == n:
                res.append(-1)
            else:
                res.append(start[idx][1])
                
        
        return res