class Solution:
    def minimumWhiteTiles(self, floor: str, c: int, L: int) -> int:
        @lru_cache(None)
        def dp(i, k):
            if i <= 0:
                return 0
            return min(dp(i-1, k) + int(floor[i-1]), dp(i-L, k-1) if k else 1000)
        
        return dp(len(floor), c)
                
        
        
        