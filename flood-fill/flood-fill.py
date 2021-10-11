class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        color = image[sr][sc]
        row, col = len(image), len(image[0])
        
        visited = set([])
        
        def dfs(r,c):
            if 0 <= r < row and 0 <= c < col and (r,c) not in visited and image[r][c] == color:
                image[r][c] = newColor
                visited.add((r,c))
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+ 1)
                dfs(r, c- 1)
            else:
                return
            
        dfs(sr, sc)
        return image
        
        
                