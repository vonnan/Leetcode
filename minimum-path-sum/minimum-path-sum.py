class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        dp = [[0] * col for _ in range(row)]
        
        for r in range(row):
            for c in range(col):
                dp[r][c] += grid[r][c]
                if r and c:
                    dp[r][c] +=  min(dp[r-1][c], dp[r][c-1])
                elif r ==0 and c:
                    dp[0][c] += dp[0][c-1]
                elif c ==0 and r:
                    dp[r][0] += dp[r-1][0]
        
        return dp[-1][-1]