class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        out = defaultdict(int)
        sets = set([])
        for u, v in roads:
            out[u] += 1
            out[v] += 1
            sets.add((u, v))
        
        res = 0
        for u in range(n):
            for v in range(u+1, n):
                tot = out[u] + out[v]
                if (u,v) in sets or (v, u) in sets:
                    tot -= 1
                res = max(res, tot)
        return res
                    
                
        
        
        
        
        