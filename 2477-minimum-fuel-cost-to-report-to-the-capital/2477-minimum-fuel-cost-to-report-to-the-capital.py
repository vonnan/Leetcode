from math import ceil

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.res = 0
        
        graph = defaultdict(set)
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)
        
        def dfs(u, prev):
            ans = 1
            
            for v in graph[u]:
                if v != prev:
                    ans += dfs(v, u)
                    
            self.res += ceil(ans/seats) if u else 0
            return ans
        
        dfs(0, 0)
        return self.res
                    
        