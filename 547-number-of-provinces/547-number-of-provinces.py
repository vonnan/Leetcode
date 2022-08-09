class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        n = len(A)
        UF = {u:u for u in range(n)}
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        
        for u in range(n):
            for v in range(u + 1, n):
                if A[u][v]:
                    union(u, v)
        
        return len(set(find(u) for u in range(n)))
                    
            