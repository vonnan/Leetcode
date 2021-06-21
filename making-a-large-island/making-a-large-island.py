class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = {0:0}
        
        def dfs(r,c, index):
            if 0 <= r <n and 0 <= c < n and grid[r][c] ==1:
                grid[r][c] = index
                return 1 + dfs(r-1, c, index) + dfs(r+1, c, index) + dfs(r, c-1, index) + dfs(r, c + 1, index)
            return 0
        
        index, res  = 2, 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] ==1:
                    area[index] = dfs(r, c, index)
                    res = max(res, area[index])
                    index += 1
                    
        path = [(0,1), (0, -1), (1,0), (-1, 0)]
        water = set([(r,c) for r in range(n) for c in range(n) if grid[r][c] ==0])
        while water:
            r,c = water.pop()
            possible = set(grid[r+dr][c + dc] for dr, dc in path if 0<=r +dr <n and 0 <= c +dc <n)
            res = max(res, sum(area[index] for index in possible) + 1)
        return res
            
        