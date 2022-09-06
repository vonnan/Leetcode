class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row, col = len(text1), len(text2)
        
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        
        for r in range(row):
            for c in range(col):
                if text1[r] == text2[c]:
                    dp[r+1][c+1] = dp[r][c] + 1
                else:
                    dp[r+1][c+1] = max(dp[r][c+1], dp[r+1][c])
                    
        return dp[-1][-1]