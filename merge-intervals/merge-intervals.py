class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        A.sort()
        res = []
        start, end = A[0]
        for s,e in A[1:]:
            if s > end:
                res.append((start, end))
                start, end = s, e
            
            else:
                end = max(end, e)
        
        res.append((start, end))
        return res
        
        