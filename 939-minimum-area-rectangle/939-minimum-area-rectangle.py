class Solution:
    def minAreaRect(self, A: List[List[int]]) -> int:
        seen = set(map(tuple,A))
        res, n = inf, len(A)
        A.sort()
        for i, a in enumerate(A):
            x1, y1 = A[i]
            for j in range(i + 1, n):
                x2, y2 = A[j]
                if x2 != x1 and y2 != y1:
                    if (x1, y2) in seen and (x2, y1) in seen:
                        res = min(res, abs(x2-x1) * abs(y2-y1))
                
        return res if res != inf else 0
                        
            
        
            
        
                
        
                
                