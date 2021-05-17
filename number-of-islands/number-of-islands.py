class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        land =set([(r,c) for r in range(m) for c in range(n) if grid[r][c] == "1"])
        res = 0
        
        while land:
            res += 1
            queue = deque([land.pop()])
            while queue:
                r, c = queue.popleft()
                for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dx, c + dy
                    if (nr, nc) in land:
                        land.remove((nr, nc))
                        queue.append((nr, nc))
        return res
        
        
        
        