class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        row, col = len(rooms), len(rooms[0])
        q = deque([])
        walls = set([])
        visited = set([])
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        level = 0
        for r in range(row):
            for c in range(col):
                if rooms[r][c] == 0:
                    q.append((r,c))
                    visited.add((r, c))
                elif rooms[r][c] == -1:
                    walls.add((r,c))
                    
        while q:
            m = len(q)
            level += 1
            for _ in range(m):
                r, c = q.popleft()
            
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited and (nr, nc) not in walls:
                        visited.add((nr, nc))
                        rooms[nr][nc] = level
                        q.append((nr, nc))
            
                    