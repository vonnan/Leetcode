
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        parent = defaultdict(set)
        for u, v in edges:
            parent[v].add(u)
            
        def dfs(node):
            visited.add(node)
            
            for p in parent[node]:
                if p not in visited:
                    dfs(p)
        
        res = []
        
        for i in range(n):
            visited = set([])
            dfs(i)
            visited.remove(i)
            res.append(sorted(visited))
        
        return res
            
