class Solution:
    def findMinArrowShots(self, A: List[List[int]]) -> int:
        if len(A) <=1:
            return len(A)
        
        res = 1
        
        A.sort()
        start, end = A[0]
        
        for s,e in A[1:]:
            if s <= end:
                end = min(end, e)
            else:
                res += 1
                end = e
        return res