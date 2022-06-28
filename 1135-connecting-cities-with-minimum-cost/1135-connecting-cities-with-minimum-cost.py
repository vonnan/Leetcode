class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        connections.sort(key = lambda x: x[2])
        UF = {i:i for i in range(1, n+ 1)}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x,x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        res = 0
        for u, v , cost in connections:
            if find(u) != find(v):
                union(u, v)
                res += cost
        
        return res
            