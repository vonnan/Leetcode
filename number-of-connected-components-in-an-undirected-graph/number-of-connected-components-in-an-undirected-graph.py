class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        UF = {i: i for i in range(n)}
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
        
        for u, v in edges:
            union(u, v)
        
        return len(set(find(i) for i in range(n)))