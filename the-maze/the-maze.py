class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        stack = [(start[0], start[1])]
        path = ((0, 1),(0, -1), (-1, 0), (1, 0))
        seen = set(stack.copy())
        while stack:
            x,y = stack.pop()
            for dx, dy in path:
                nx , ny = x,y
                while 0<= nx <m and 0<= ny < n and maze[nx][ny] ==0:
                    nx += dx
                    ny += dy
                nx -= dx
                ny -= dy
                if destination ==[nx,ny]:
                    return True
                if (nx, ny) not in seen:
                    stack.append((nx,ny))
                    seen.add((nx, ny))
        return False
                    
            
        
                
            
                
            