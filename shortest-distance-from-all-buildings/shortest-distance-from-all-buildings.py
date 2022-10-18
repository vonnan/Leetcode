class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        houses = set([(r,c) for r in range(row) for c in range(col) if grid[r][c] == 1])
        dic = defaultdict(list)
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        for house in houses:
            r, c = house
            q = deque([(r,c, 0)])
            seen = set([(r, c)])
            while q:
                r,c,d = q.popleft()
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and ((nr, nc) not in seen) and grid[nr][nc] == 0:
                        dic[(nr, nc)].append(d + 1)
                        seen.add((nr, nc))
                        q.append((nr, nc, d + 1))
        n = len(houses)
        
        if not dic:
            return -1
        
        lst = [sum(val) for val in dic.values() if len(val) == n]
        if not lst:
            return -1
        return min(lst)
                
        
        