class Solution:
    def makeConnected(self, n: int, A: List[List[int]]) -> int:
        if len(A) < n-1:
            return -1
        
        UF = {i: i for i in range(n)}
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
        
        for a,b in A:
            union(a, b)
        
        return len(set([find(i) for i in range(n)])) - 1