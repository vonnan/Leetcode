from collections import defaultdict
class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        if A[0][0] ==1:
            return 0
        
        row, col = len(A), len(A[0])
        
        dp =[[0] * col for _ in range(row)]
        dp[0][0] = 1
        
        for r in range(row):
            for c in range(col):
                if not A[r][c]:
                    if r > 0:
                        dp[r][c] += dp[r-1][c]
                    if c > 0:
                        dp[r][c] += dp[r][c-1]
                
        
        return dp[-1][-1]