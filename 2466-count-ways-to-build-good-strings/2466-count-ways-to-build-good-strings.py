class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        
        dp = [0] * (high + 1)
        mod = 10 ** 9 + 7
        dp[0] = 1
        for i in range(high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= mod
            
        dp = list(accumulate(dp))
        return (dp[-1] - dp[low-1]) % (mod)
            