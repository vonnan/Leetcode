class Solution:
    def nearestExit(self, maze: List[List[str]], A: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        r,c = A
        q = deque([(r,c)])
        
        visited = set([(r, c)])
        res = 0
        while q:
            m = len(q)
            res += 1
            for _ in range(m):
                r,c = q.popleft()
                
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in visited:
                        continue
                    elif nr <0 or nr >= row or nc < 0 or nc >= col:
                        continue
                    elif maze[nr][nc] == "+":
                        continue
                    elif nr == 0 or nr == row - 1 or nc == 0 or nc == col -1:
                        return res
                    else:
                        q.append((nr, nc))
                        visited.add((nr, nc))
        return -1
                        
            