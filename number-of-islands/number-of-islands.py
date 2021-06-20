class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        land = set([(i,j) for i in range(row) for j in range(col) if grid[i][j] == "1"])
        res = 0
        path = [(0,1), (1,0), (-1,0), (0, -1)]
        
        while land:
            res += 1
            queue = deque([land.pop()])
            while queue:
                r,c = queue.popleft()
                for dr, dc in path:
                    nr, nc = r + dr, c +dc
                    if (nr, nc) in land:
                        queue.append((nr, nc))
                        land.remove((nr, nc))
        return res
                        