class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row= col = len(grid)
        tot = row * row
        
        land = [(r,c) for r in range(row) for c in range(col) if grid[r][c]]
        if not land:
            return -1
        
        q = deque(land)
        if len(land) == tot:
            return -1
        
        
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        seen = set(land)
        res = 0
        
        while q:
            m = len(q)
            res += 1
            for _ in range(m):
                r, c = q.popleft()
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        q.append((nr, nc))
                        if len(seen) == tot:
                            return res
        
                    
                
             
            