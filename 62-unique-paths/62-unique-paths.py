class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for r in range(m):
            for c in range(n):
                if r > 0:
                    dp[r][c] += dp[r-1][c]
                if c > 0:
                    dp[r][c] += dp[r][c-1]
        
        return dp[-1][-1]