class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 1
        points.sort()
        
        end = points.pop(0)[1]
        for s,e in points:
            if s > end:
                res += 1
                end = e
            else:
                end = min(end, e)
        return res