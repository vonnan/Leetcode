class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n+1):
            dp[i] = sum(dp[j] * dp[i-1-j] for j in range(i))
        return dp[-1]