class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
            
        UF = list(range(n+1))
        res, e1, e2 = 0, 0, 0
        for t, a, b in edges:
            if t == 3:
                if find(a) != find(b):
                    e1 += 1
                    e2 += 1
                    UF[find(a)] = find(b)
                else:
                    res += 1
        
        UFa = UF[:]
        
        for t, a, b in edges:
            if t == 1:
                if find(a) == find(b):
                    
                    res += 1
                    
                else:
                    UF[find(a)] = find(b)
                    e1 += 1
                    
        UF = UFa[:]
        
        for t, a, b in edges:
            if t == 2:
                if find(a) != find(b):
                    UF[find(a)] = find(b)
                    e2 += 1
                    
                else:
                    
                    res += 1
        
        if e1 == n-1 and e2 == n-1:
            return res
        else:
            return -1
        
        

        
        
       
            
        
        
                
            
        
        