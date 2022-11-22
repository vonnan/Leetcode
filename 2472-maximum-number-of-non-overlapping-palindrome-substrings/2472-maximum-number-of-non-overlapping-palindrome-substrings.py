class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def Pal(i, j):
            if i <0 or j <= i:
                return False
            
            return s[i:j] == s[i:j][::-1]
        
        n = len(s)
        dp = [0] * (n + 1)
        for j in range(k, n + 1):
            dp[j] = dp[j-1]
            if Pal(j - k, j):
                dp[j] = max(dp[j], 1 + dp[j - k])
            elif Pal(j - k - 1, j):
                dp[j] = max(dp[j], 1 + dp[j - k - 1])
        return dp[-1]
        
        
        