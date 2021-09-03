class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        color = image[sr][sc]
        row, col = len(image), len(image[0])
        visited = set()
        def dfs(r, c):
            if (r,c) not in visited and 0 <= r < row and 0 <= c < col and image[r][c] == color:
                image[r][c] = newColor
                visited.add((r, c))
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)
            else:
                return
        
        dfs(sr, sc)
        
        return image