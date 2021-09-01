class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        row= len(isConnected)
        
        for r in range(row):
            for c in range(row):
                if isConnected[r][c] == 1:
                    union(r, c)
        
        return len(set([find(r) for r in range(row)]))
        