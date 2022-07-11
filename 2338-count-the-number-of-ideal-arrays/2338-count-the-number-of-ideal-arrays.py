class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10 **9 + 7
        
        @lru_cache(None)
        def dp(last, k):
            res = math.comb(n-1, k-1) % mod
            if k == n:
                return res % mod
            
            for j in range(2*last, maxValue +1, last):
                res += dp(j, k + 1)
            return res
        
        res = 0
        for last in range(1, maxValue+1):
            res += dp(last, 1) % mod
        
        return res % mod
        