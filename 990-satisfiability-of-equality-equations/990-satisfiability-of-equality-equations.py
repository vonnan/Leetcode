class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        UF = { }
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        
        
        equal, un = [(x[0], x[-1]) for x in equations if x[1] == "="],  [(x[0], x[-1]) for x in equations if x[1] == "!"]
        
        for a, b in equal:
            union(a, b)
            
        for a, b in un:
            if a == b:
                return False
            
            if a in UF and b in UF and find(a) == find(b):
                return False
        
        return True
        
            