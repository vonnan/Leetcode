class Solution:
    def checkRecord(self, n: int) -> int:
    
        dp = [1,2,4]
        mod = 10 ** 9 + 7
        if n== 1:
            return 3
        
        for _ in range(3, n+ 1):
            dp.append((dp[-1]+ dp[-2] + dp[-3]) % mod)
        
        for i in range(1, n + 1):
            dp[-1] += dp[i - 1] * dp[n-i]
        
        return dp[n] % mod
        
            
        
        
              
        