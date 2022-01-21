class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0]* (k +1) for _ in range(n + 1)]
        for r in range(n):
            for c in range(k):
                dp[r+1][c+1] = dp[r][c] + dp[r][c+1] + 1
                if dp[r+1][c+1] >=n:
                    return r+ 1
        
