from collections import Counter
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        UF = [i for i in range(n)]
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF[find(x)] = find(y)
            
        for a,b in edges:
            union(a, b)
        
        for i in range(n):
            find(i)
        
        return len(set(UF))
        
            
                        
        