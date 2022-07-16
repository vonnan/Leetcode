class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        
        old = image[sr][sc]
        image[sr][sc] = color
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        q = deque([(sr, sc)])
        
        visited = set([(sr, sc)])
        
        while q:
            m = len(q)
            for _ in range(m):
                r, c = q.popleft()
                
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and image[nr][nc] == old and (nr, nc) not in visited:
                        image[nr][nc] = color
                        q.append((nr, nc))
                        visited.add((nr, nc))
        
        return image
                    