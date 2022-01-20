class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(None)
        def dp(mask, pos):
            if pos == 0:
                return 1
            
            res = 0
            for i in range(n):
                if mask & ( 1<< i) and (not pos % (i + 1) or not (i + 1) % pos):
                    res += dp(mask ^ (1 <<i), pos -1)
            
            return res
        
        return dp((1<<n) -1, n)
                    