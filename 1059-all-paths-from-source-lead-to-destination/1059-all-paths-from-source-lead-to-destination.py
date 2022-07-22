class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            
        seen = set([])
        
        def dfs(u):
            seen.add(u)
            for v in graph[u]:
                if u == v or (v in seen) or (not dfs(v)):
                    return False
            
            seen.discard(u)
            return graph[u] or u == destination
        
        return dfs(source)