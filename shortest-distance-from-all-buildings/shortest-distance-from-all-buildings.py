class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        houses, res, reach  = set([]), inf, defaultdict(list)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    houses.add((r,c, 0))
                elif grid[r][c]== 0:
                    reach[(r,c)] = []
                    
        for house in houses:
            
            q = deque([house])
            seen = set()
            
            while q:
                r, c, dist = q.popleft()
                
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    
                    if ((nr, nc) not in seen) and (0 <= nr < row) and (0 <= nc < col) and grid[nr][nc] == 0:
                        seen.add((nr, nc))
                        q.append((nr, nc, dist + 1))
                        reach[(nr,nc)].append(dist + 1)
                    
       
        n = len(houses)
        for key, val in reach.items():
            if len(val) == n:
                res = min(res, sum(val))
        return res if res != inf else -1
                    