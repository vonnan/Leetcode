class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
        
        n = len(isConnected)
        
        for r in range(n):
            for c in range(n):
                if isConnected[r][c] == 1:
                    union(r,c)
        
        return len(set(find(i) for i in range(n)))