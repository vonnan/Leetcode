class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        UF = {i: i for i in range(n)}
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        for u, v in edges:
            union(u, v)
        
        return find(source) == find(destination)