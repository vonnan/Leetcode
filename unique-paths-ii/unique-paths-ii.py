from collections import defaultdict
class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        if A[0][0] ==1:
            return 0
        
        row, col = len(A), len(A[0])
        
        path = [(0,1), (1, 0)]
        
        dp =[[0] * col for _ in range(row)]
        dp[0][0] = 1
        for c in range(1, col):
            dp[0][c] = dp[0][c-1] * (1- A[0][c])  
        
        for r in range(1, row):
            dp[r][0] = dp[r-1][0] * (1-A[r][0])
        
        for r in range(1,row):
            for c in range(1,col):
                if A[r][c] == 1:
                    dp[r][c] = 0
                    continue
                dp[r][c] = dp[r][c-1] + dp[r-1][c]
                
        
        return dp[-1][-1]