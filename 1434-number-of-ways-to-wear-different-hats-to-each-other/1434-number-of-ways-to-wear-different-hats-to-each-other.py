class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        h2p = defaultdict(set)
        
        for p, hs in enumerate(hats):
            for h in hs:
                h2p[h].add(p)
        
        mod = 10 **9 + 7
        
        @lru_cache(None)
        def ct(h, mask):
            if mask == 0:
                return 1
            
            if h == 41:
                return 0
            
            res = ct(h + 1, mask)
            
            for p in h2p[h]:
                if mask & (1 <<p):
                    res += ct(h + 1, mask ^ (1 << p))
                    res %= mod
                    
            return res
        
        return ct(1, (1<<n) - 1)