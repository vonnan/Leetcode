class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0]
        res = []
        
        for s,e in intervals[1:]:
            if s > end:
                res.append((start, end))
                start, end = s, e
            else:
                end = max(e, end)
        
        res.append((start, end))
        return res