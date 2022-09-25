class Solution:
    def removeInterval(self, A: List[List[int]], B: List[int]) -> List[List[int]]:
        A.sort()
        start, end = B
        
        res = []
        
        for i in range(len(A)):
            s,e = A[i]
            if e <= start:
                res.append([s,e])
                continue
            elif s >= end:
                return res + A[i:]
            if s < start:
                res.append([s, start])
            if e > end:
                res.append([end, e])
                if i < len(A) - 1:
                    return res + A[i + 1:]
         
        return res
                