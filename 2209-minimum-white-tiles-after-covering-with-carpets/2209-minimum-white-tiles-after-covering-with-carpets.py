class Solution:
    def minimumWhiteTiles(self, floor: str, c: int, L: int) -> int:
        ct = floor.count("1")
        @lru_cache(None)
        def dp(i, k):
            if i < 0:
                return 0
            if k < 0:
                return inf
            return min(dp(i-1, k) + int(floor[i]), dp(i-L, k-1) if k else ct)
        
        return dp(len(floor) - 1, c)
                
        
        
        