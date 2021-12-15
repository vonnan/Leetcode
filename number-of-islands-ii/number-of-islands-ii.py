class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        UF= {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
                
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
        
        res = [1]
        r,c = positions[0]
        UF[(r,c)] = (r,c)
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        for r,c in positions[1:]:
            if (r,c) in UF:
                res.append(res[-1])
                continue
            UF.setdefault((r,c), (r,c))
            sets = set([])
            for dr, dc in path:
                nr, nc = r + dr, c + dc
                if (nr,nc) in UF:
                    sets.add((nr, nc))
            res.append(res[-1] + 1 - len(set(find((nr, nc)) for (nr, nc) in sets)))
            for nr, nc in sets:
                union((r,c), (nr, nc))
                
        return res
                    