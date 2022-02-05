class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n-2, -1, -1):
            piles[i] += piles[i+1]
        
        @lru_cache(None)
        def dp(pos, m):
            if pos + 2*m >= n:
                return piles[pos]
            return piles[pos] - min(dp(pos + i, max(m, i)) for i in range(1, 2*m + 1))
    
        return dp(0,1)
            