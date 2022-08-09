class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        UF = {}
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        for r,c in stones:
            union(r, ~c)
        
        return len(stones) - len(set(find(r) for r,c in stones))