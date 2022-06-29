class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        path = [(0,1), (0, -1), (1,0), (-1,0)]
        row, col = len(grid), len(grid[0])
        food = set([])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "*":
                    start = (r,c)
                elif grid[r][c] == "#":
                    food.add((r,c))
        visited = set([start])
        
        q = deque([start])
        step = 0
        while q:
            m = len(q)
            step += 1
            for _ in range(m):
                r,c = q.popleft()
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited and grid[nr][nc] !=  "X":
                        visited.add((nr,nc))
                        if grid[nr][nc] == "#":
                            food.remove((nr, nc))
                            
                            return step
                        q.append((nr, nc))
        return -1