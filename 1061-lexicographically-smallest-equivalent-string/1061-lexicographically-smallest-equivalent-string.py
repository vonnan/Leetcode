class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        UF = {}
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
        
        for a,b in zip(s1,s2):
            union(a,b)
            
        children = defaultdict(set)
        
        for key, val in UF.items():
            children[find(key)].add(key)
            
        dic = {}
        for key, val in children.items():
            dic[key] = sorted(list(val))[0]
        
        res = ""
        for c in baseStr:
            if c in UF:
                res += dic[find(c)]
            else:
                res += c
        
        return res
        
        