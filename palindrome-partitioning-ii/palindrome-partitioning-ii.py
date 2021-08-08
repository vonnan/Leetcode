class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(-1, n)]
        for i in range(n):
            for j in range(i, n):
                if s[i:j + 1] == s[i:j+1][::-1]:
                    dp[j + 1] = min(dp[j + 1], dp[i] + 1)
        return dp[-1]