from bisect import bisect_left
from bisect import insort
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        row, col = len(matrix), len(matrix[0])
        
        for r in range(row):
            for c in range(1, col):
                matrix[r][c] += matrix[r][c-1]
                
        res = -inf
        print(matrix)
        for c1 in range(col):
            for c2 in range(c1, col):
                arr = [matrix[r][c2] - (matrix[r][c1-1] if c1>0 else 0) for r in range(row)]
                curr = 0
                presum =[-inf,inf]
                for a in arr:
                    insort(presum, curr)
                    curr += a
                    idx = bisect_left(presum, curr- k)
                    res = max(res, curr - presum[idx])

        return res 

     
        
        
                
                