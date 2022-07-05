
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = deque([(0, 0, 0)])
        row, col = len(grid), len(grid[0])
        if row == 1 and col == 1:
            return 0
        
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        dic = defaultdict(int)
        dic[(0,0)] = 0
        
        level = 0
        while q:
            m = len(q)
            for _ in range(m):
                r,c,obs = q.popleft()
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if nr == row -1 and nc == col -1:
                        return level + 1
                    if 0 <= nr < row and 0 <= nc < col and ((nr, nc) not in dic or dic[(nr, nc)] > obs):
                        if grid[nr][nc]:
                            if obs + 1 > k:
                                continue
                            elif (nr, nc) not in dic or dic[(nr, nc)] > obs + 1:
                                dic[(nr, nc)] = obs + 1
                                q.append((nr, nc, obs + 1))
                        else:
                            if (nr, nc) not in dic or dic[(nr, nc)] > obs:
                                dic[(nr, nc)] = obs
                                q.append((nr, nc, obs))
            level += 1
            
        return -1
                        
                                
