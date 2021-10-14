class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        rotten, fresh = set([]), set([])
        res = -1
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    rotten.add((r,c))
                elif grid[r][c] ==1:
                    fresh.add((r,c))
        if not fresh:
            return 0
        if fresh and not rotten:
            return -1
        q = deque(list(rotten))
        
        while q:
            m = len(q)
            for _ in range(m):
                r,c = q.popleft()
                
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten.add((nr, nc))
                        q.append((nr, nc))
                        fresh.remove((nr, nc))
            res += 1
        if fresh:
            return -1
        else:
            return res 
        