class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = max((text1[i]==text2[j])+ dp[i][j], dp[i+1][j], dp[i][j+1])
        
        return dp[m][n]