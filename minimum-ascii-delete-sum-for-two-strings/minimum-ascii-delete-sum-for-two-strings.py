class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        row, col = len(s1), len(s2)
        
        dp = [[0]* (col + 1) for _ in range(row + 1)]
        
        for r in range(row):
            for c in range(col):
                if s1[r] == s2[c]:
                    dp[r+1][c+1] = dp[r][c] + ord(s1[r])
                else:
                    dp[r+1][c+1] = max(dp[r][c+1] , dp[r+1][c])
        
        return sum(map(ord,s1+ s2)) - dp[-1][-1] * 2