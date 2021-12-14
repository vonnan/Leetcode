class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        n = len(A)
        
        for r in range(n):
            for c in range(r, n):
                if A[r][c]:
                    union(r, c)
                
        return len(set(find(i) for i in range(n)))