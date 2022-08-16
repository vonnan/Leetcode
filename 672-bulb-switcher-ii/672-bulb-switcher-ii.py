class Solution:
    def flipLights(self, n: int, p: int) -> int:
        
        states = [1] * n
        res = set([tuple(states)])
        
        for _ in range(p):
            sets = set([])
            for x in res:
                new = list(x)
                for i in range(0,n, 2):
                    new[i] = 1- new[i]
                sets.add(tuple(new))
                
                new = list(x)
                for i in range(1, n, 2):
                    new[i] = 1- new[i]
                sets.add(tuple(new))
                
                new = list(x)
                for i in range(n):
                    new[i] = 1 -new[i]
                sets.add(tuple(new))
                
                new = list(x)
                for i in range(0, n, 3):
                    new[i] = 1- new[i]
                sets.add(tuple(new))
            
            res = sets
        
        return len(res)
                
                
        
        
            