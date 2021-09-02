class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        UF = {}
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)
            
        path =[(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = [1]
        
        UF.setdefault((positions[0][0], positions[0][1]), (positions[0][0], positions[0][1]))
        for r, c in positions[1:]:
            if (r,c) in UF:
                res.append(res[-1])
                continue
    
            UF.setdefault((r, c), (r, c))
            sets = set()
            for dr, dc in path:
                nr, nc = r+ dr, c + dc
                if (nr, nc) in UF:
                    sets.add((nr, nc))
                          
            res.append(res[-1] - len(set(find((nr, nc)) for (nr, nc) in sets)) + 1)
            
            for (nr, nc) in sets:
                union((nr, nc), (r, c))
            
        return res
                
                        
        
                
                
                
                    