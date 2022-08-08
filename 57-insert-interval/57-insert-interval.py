from bisect import bisect_left

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        idx = bisect_left(intervals, newInterval)
        intervals.insert(idx, newInterval)
        start, end = intervals[0]
        for s,e in intervals[1:]:
            if s > end:
                res.append((start, end))
                start, end = s, e
            else:
                end = max(e, end)
        res.append((start, end))
        return res
        