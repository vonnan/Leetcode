class Solution:
    def waysToDistribute(self, n: int, k: int) -> int:
        dp = [[0] * (n+1) for _ in range(k + 1)]
        mod = 10 ** 9 + 7
        
        dp[0][0] = 1
        
        for r in range(1, k+1):
            for c in range(r, n+ 1):
                dp[r][c] = r * dp[r][c-1] + dp[r-1][c-1]
        
        return dp[-1][-1] % mod
                
                