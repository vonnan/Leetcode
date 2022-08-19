from random import randint

class Solution:
    def new21Game(self, n: int, k: int, W: int) -> float:
        if k == 0 or k + W <= n:
            return 1.0
            
        dp = [1] + [0] * n
        
        Wsum = 1
        
        for i in range(1, n + 1):
            dp[i] = Wsum / W
            if i < k:
                Wsum += dp[i]
            if i >= W:
                Wsum -= dp[i - W]
        
        return sum(dp[k:])
            
