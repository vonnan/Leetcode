from bisect import bisect_right
from bisect import insort

class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        if len(mines) == N*N:
            return 0
        
        row = [[-1, N] for _ in range(N)]
        col = [[-1, N] for _ in range(N)]
        
        for r,c in mines:
            insort(row[r], c)
            insort(col[c], r)
            
        res = 0
        
        for r in range(N):
            for i in range(len(row[r])-1):
                left = row[r][i]
                right = row[r][i+1]
                for c in range(left + 1 + res, right - res):
                    idx = bisect_right(col[c], r)
                    up = col[c][idx-1]
                    down = col[c][idx]
                    res = max(res, min(r- up, down -r, c - left, right -c))
                    
        return res
            
        
        
