class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        
        intervals.sort(key = lambda x: x[1])
        
        end = intervals[0][1]
        res = 0
        for s,e in intervals[1:]:
            if s >= end:
                end = e
            else:
                res += 1
        return res

        