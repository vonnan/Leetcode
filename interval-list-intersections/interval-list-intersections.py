class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        m, n = len(A), len(B)
        res = []
        while i < m and j < n:
            la, ra = A[i]
            lb, rb = B[j]
            
            if la > rb:
                j += 1
            
            elif lb > ra:
                i += 1
                
            else:
                l = max(la, lb)
                r = min(ra, rb)
                res.append((l, r))
                i += 1
                j += 1
                if rb > r:
                    B.insert(j, [r, rb])
                    n += 1
                if ra > r:
                    A.insert(i, [r, ra])
                    m += 1
        
        return res