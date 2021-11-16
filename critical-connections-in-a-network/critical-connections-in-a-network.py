class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        edges = defaultdict(set)
        for u, v in connections:
            edges[u].add(v)
            edges[v].add(u)
            
        low = [0] * n
        
        def dfs(rank, child, parent):
            low[child], res = rank, []
            for nei in edges[child]:
                if nei != parent:
                    if not low[nei]:
                        res += dfs(rank + 1,  nei, child)
                    low[child] = min(low[child], low[nei])
                    if low[nei] == rank + 1:
                        res.append((child, nei))
            return res
        
        return dfs(1, 0, -1)
        
        