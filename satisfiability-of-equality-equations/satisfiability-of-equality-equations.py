class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
        
        q = deque([])
        for s in equations:
            if s[1] == "!":
                if s[0] == s[-1]:
                    return False
                q.append((s[0], s[-1]))
                
            else:
                union(s[0], s[-1])
                
        while q:
            a,b = q.pop()
            if a not in UF or b not in UF:
                continue
            if find(a) == find(b):
                return False
            
        return True