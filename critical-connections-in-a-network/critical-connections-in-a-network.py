class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(rank, curr, prev):
            low[curr] = rank
            for neighbor in edges[curr]:
                if neighbor == prev:
                    continue
                
                if not low[neighbor]:
                    dfs(rank + 1, neighbor, curr)
                
                low[curr] = min(low[curr], low[neighbor])
                
                if low[neighbor] == rank + 1:
                    res.add((curr, neighbor))
                    
        low, res, edges = [0] * n, set([]), defaultdict(list)
        
        for u,v in connections:
            edges[u].append(v)
            edges[v].append(u)
        
        dfs(1, 0, -1)
        return res