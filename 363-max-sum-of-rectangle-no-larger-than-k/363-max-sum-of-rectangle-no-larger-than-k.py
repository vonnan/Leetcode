from sortedcontainers import SortedList
from bisect import bisect_left
from bisect import insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        
        for r in range(row):
            matrix[r] = [0] + matrix[r]
            for c in range(1, col + 1):
                matrix[r][c] += matrix[r][c-1]
        
        res = -inf
        
        for c1 in range(col):
            for c2 in range(c1 +1, col + 1):
                arr = [matrix[r][c2] - matrix[r][c1] for r in range(row)]
                presum = [-inf,0,  inf]
                pre = 0
                for a in arr:
                    pre += a
                    idx = bisect_left(presum, pre - k)
                    if pre - presum[idx] > res:
                        res = pre - presum[idx]
                        if res == k:
                            return res
                    insort(presum, pre)
        return res
                
                    
                    
                    
        
        
        