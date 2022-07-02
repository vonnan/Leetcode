class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
        
        row, col = len(grid), len(grid[0])
        
        dic_r, dic_c = defaultdict(list), defaultdict(list)
        sets = set([])
        ct = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    dic_r[r].append(c)
                    dic_c[c].append(r)
                   
        
        for r, lst in dic_r.items():
            if len(lst) > 1:
                for c in lst:
                    sets.add((r, c))
        
        for c, lst in dic_c.items():
            if len(lst) >1:
                for r in lst:
                    sets.add((r, c))
        
        
        return len(sets)
                    