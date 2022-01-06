class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        row, col = len(A), len(A[0])
        dp = [[0] * col for _ in range(row)]
        if A[0][0]:
            return 0
        
        dp[0][0] = 1
        
        for r in range(row):
            for c in range(col):
                if A[r][c]:
                    continue
                
                if r:
                    dp[r][c] += dp[r-1][c]
                if c:
                    dp[r][c] += dp[r][c-1]
                    
        return dp[-1][-1]
        