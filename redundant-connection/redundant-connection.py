class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        UF = {}
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        for x,y in edges:
            if x in UF and y in UF and find(x) == find(y):
                ans =(x, y)
            else:
                union(x,y)
                
        return ans