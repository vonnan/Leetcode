class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        
        for i, c in enumerate(s[1:], 1):
            if c == "0":
                if s[i-1] == "0" or s[i-1] >= "3":
                    return 0
                
                else:
                    dp[i + 1] += dp[i-1]
            
            else:
                dp[i + 1] += dp[i]
                if 10 <= int(s[i-1: i+1]) <= 26:
                    dp[i+1] += dp[i-1]
        return dp[-1]
        
                    
                    
            