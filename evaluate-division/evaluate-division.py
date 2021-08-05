class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
       
        for (u,v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1/val
            
        def dfs(p, q, visited):
            
            if p not in graph or q not in graph:
                return -1.0
            
            if p == q:
                return 1.0
            
            if q in graph[p]:
                return graph[p][q]
            
            for v in graph[p]:
                if v not in visited:
                    visited.add(v)
                    temp = dfs(v, q, visited)
                    if temp == -1.0:
                        continue
                    else:
                        return temp * graph[p][v]
            return -1.0
        res = []
        for p, q in queries:
            res.append(dfs(p, q, set()))
        return res
                    
                        
            
        
        
            
                
        
        