from collections import Counter
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        for a,b in edges:
            union(a, b)
        
        return len(set(find(i) for i in range(n) if i in UF)) + sum(i not in UF for i in range(n))
        
            
                        
        