class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            if n ==1:
                return True 
            else:
                return False
        
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x,x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        for a,b in edges:
            if a in UF and b in UF and find(a) == find(b):
                return False
            union(a,b)
        
        
        return len(set(find(i) for i in range(n) if i in UF)) + sum(i for i in range(n) if i not in UF) == 1
        