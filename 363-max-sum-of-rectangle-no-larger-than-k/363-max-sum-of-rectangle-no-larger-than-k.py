from bisect import bisect_left
from bisect import insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        
        for r in range(row):
            matrix[r] = list(accumulate(matrix[r], initial = 0))
        
        res = -inf
        for c1 in range(col):
            for c2 in range(c1 + 1, col + 1):
                arr = [matrix[r][c2] - matrix[r][c1] for r in range(row)]
                presum = [0]
                pre = 0
                for a in arr:
                    nxt = pre + a
                    idx = bisect_left(presum, nxt - k)
                    if idx < len(presum):
                        res = max(res, nxt - presum[idx])
                        if res == k:
                            return k
                    pre = nxt
                    insort(presum, nxt)
        return res
                    
                
                       