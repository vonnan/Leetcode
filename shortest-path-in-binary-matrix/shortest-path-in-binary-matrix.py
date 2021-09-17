class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        path = [(0,1), (0, -1), (1, 0), (-1, 0), (-1,1), (1,1), (1, -1), (-1, -1)]
        if grid==[[0]]:
            return 1
        if grid[0][0] == 1 or grid[-1][-1] ==1:
            return -1
        n = len(grid)
        q = deque([(0,0)])
        target = (n-1, n-1)
        visited = set([])
        res = 1
        while q:
            m = len(q)
            res += 1
            for _ in range(m):
                r,c = q.popleft()
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) not in visited and (0 <= nr < n) and (0 <= nc < n) and (grid[nr][nc] == 0):
                        visited.add((nr, nc))
                        grid[nr][nc] = 1
                        q.append((nr, nc))
                        
                        if nr == n-1 and nc== n-1:
                            return res
        return -1