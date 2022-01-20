class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n, mod = len(hats), 10 ** 9 + 7
        
        h2p = defaultdict(set)
        
        for p, hs in enumerate(hats):
            for h in hs:
                h2p[h-1].add(p)
                
        @lru_cache(None)
        def dp(mask, h):
            if mask == 0:
                return 1
            
            if h == 40:
                return 0
            
            res = dp(mask, h + 1)
            for p in h2p[h]:
                if mask & (1 <<p):
                    mask_nxt = mask ^ ( 1<<p)
                    res += dp(mask_nxt, h + 1)
                    res %= mod
            
            return res
        
        return dp((1 <<n) - 1, 0)