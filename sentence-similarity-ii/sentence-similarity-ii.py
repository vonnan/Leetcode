class Solution:
    def areSentencesSimilarTwo(self, s1: List[str], s2: List[str], pairs: List[List[str]]) -> bool:
        if len(s1) != len(s2):
            return False
        
        UF = {}
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
        
        for w1,w2 in pairs:
            union(w1, w2)
            
        return all(w1 == w2 or (w1 in UF and w2 in UF and find(w1) == find(w2)) for w1, w2 in zip(s1,s2))