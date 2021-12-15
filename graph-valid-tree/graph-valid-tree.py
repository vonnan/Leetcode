class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        UF = {i: i for i in range(n)}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        for a,b in edges:
            if find(a) == find(b):
                return False
            else:
                n-= 1
                union(a,b)
        return n==1