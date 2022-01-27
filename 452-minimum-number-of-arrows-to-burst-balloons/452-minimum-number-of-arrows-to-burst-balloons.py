class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        A.sort()
        start, end = A[0]
        res = 1
        
        for s,e in A[1:]:
            if s <= end:
                end = min(e, end)
            else:
                res += 1
                end = e
        return res