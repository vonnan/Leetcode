class Solution:
    def minimumWhiteTiles(self, floor: str, c: int, L: int) -> int:
        
        @lru_cache(None)
        def dp(i, k):
            if k < 0:
                return inf
            
            if i < 0:
                return 0
            
            return min(dp(i-L, k-1), dp(i-1, k) + int(floor[i]))
        
        return dp(len(floor) - 1, c)
                
        
        
        