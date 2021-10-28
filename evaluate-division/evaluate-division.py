class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for u, v in equations:
            graph[u][v] = values.pop(0)
            graph[v][u] = 1/graph[u][v]
            
        def dfs(p,q, visited):
            if p not in graph or q not in graph:
                return -1.0
            if p == q:
                return 1.0
            
            if q in graph[p]:
                return graph[p][q]
            
            for v in graph[p]:
                if v not in visited:
                    visited.add(v)
                    tmp = dfs(v, q, visited)
                    if tmp == -1.0:
                        continue
                    else:
                        return tmp * graph[p][v]
            return -1.0
        
        res = []
        for u,v in queries:
            res.append(dfs(u, v, set([])))
        return res
                
                    
                        
            
        
        
            
                
        
        