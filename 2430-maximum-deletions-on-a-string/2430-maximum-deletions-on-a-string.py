class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return len(s)
        
        if n == len(set(s)):
            return 1
        
        dp = [1] * ( n + 1)
        
        for i in range(n, -1, -1):
            for d in range(1, min(n - i, i)+ 1):
                if s[i:i + d] == s[i - d :i]:
                    dp[i - d] = max(dp[i-d], dp[i] + 1)
        
        return dp[0]
            