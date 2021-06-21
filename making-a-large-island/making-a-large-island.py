class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n= len(grid)
        area = {0: 0}
        
        def dfs(r,c, index):
            if 0 <= r <n and 0 <= c < n and grid[r][c] ==1:
                grid[r][c] = index
                area[index] =  1 + dfs(r-1, c, index) + dfs(r+1, c, index) + dfs(r, c-1, index) + dfs(r, c + 1, index)
                return area[index]
            return 0
        
        
        
        index = 2
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r,c,index)
                    index += 1
        
        res = max(area.values())
        path = [(0,1), (0,-1), (1,0), (-1,0)]
        for r in range(n):
            for c in range(n):
                if grid[r][c] ==0:
                    nei_index = set(grid[r+dr][c+dc] for dr, dc in path if 0 <= r+dr < n and 0 <= c+dc < n)
                    res = max(res, sum(area[index] for index in nei_index) + 1)
                    
        return res
        
        
        
        
        