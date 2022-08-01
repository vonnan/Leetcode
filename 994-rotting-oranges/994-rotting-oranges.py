class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        rotten, fresh = set([]), set([])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    rotten.add((r, c))
                elif grid[r][c] == 1:
                    fresh.add((r,c))
        if not fresh:
            return 0
        
        n = len(rotten) + len(fresh)
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        q = deque(list(rotten))
        res = 0
        
        while q:
            m = len(q)
            res += 1
            for _ in range(m):
                r, c = q.popleft()
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten.add((nr, nc))
                        if len(rotten) == n:
                            return res
                        
                        q.append((nr, nc))
        
        return -1
        
        