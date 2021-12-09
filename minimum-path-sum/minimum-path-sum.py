class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        dp = [[0] * col for _ in range(row)]
        
        for r in range(row):
            for c in range(col):
                if r ==0 and c == 0:
                    dp[r][c] = grid[r][c]
                elif r == 0:
                    dp[r][c] = dp[r][c-1] + grid[r][c]
                elif c == 0:
                    dp[r][c] = dp[r-1][c] + grid[r][c]
                else:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
                    
        return dp[-1][-1]