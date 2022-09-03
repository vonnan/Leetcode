class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
                    
        for r in range(n):
            for c in range(n):
                if grid[r][c]== 1:
                    start = r, c
                    break
        r,c = start
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        print(r, c)
        start = r, c
        seen = set([])
        def dfs(r,c):
            if 0 <= r < n and 0 <= c < n and (r,c) not in seen and grid[r][c] == 1:
                grid[r][c] = 2
                seen.add((r, c))
                dfs(r, c + 1)
                dfs(r, c - 1)
                dfs(r + 1, c)
                dfs(r - 1, c)
                
        res = 2 * n
        
        dfs(r, c)
        print(grid)
        step = 0
        
        while seen:
            new = set([])
            
            for r, c in seen:
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            return step
                        elif not grid[nr][nc]:
                            grid[nr][nc] = 2
                            new.add((nr, nc))
            step += 1
            seen = new
            
            
        
           
        
        
                
                
                
        