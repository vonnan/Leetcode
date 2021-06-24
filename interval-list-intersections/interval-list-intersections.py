from bisect import bisect
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        m, n = len(A), len(B)
        
        while i < m and j < n:
            l1, r1 = A[i]
            l2, r2 = B[j]
            
            left = max(l1, l2)
            
            if r1 < r2:
                i += 1
                if left <= r1:
                    res.append((left, r1))
                    
            else:
                j += 1
                if left <= r2:
                    res.append((left, r2))
                    
        return res
            
                
            
                    
        
        