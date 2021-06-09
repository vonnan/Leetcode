class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        path = [(0,1), (0, -1), (1, 0), (-1,0)]
        heap = [(0, start[0], start[1])]
        visited = set()
        
        while heap:
            cost, x,y = heappop(heap)
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if destination ==[x,y]:
                return cost
            
            for dx, dy in path:
                nx, ny = x, y
                nw = 0
                while 0 <= nx < row and 0 <= ny < col and maze[nx][ny] == 0:
                    nx += dx
                    ny += dy
                    nw += 1
                nx -= dx
                ny -= dy
                nw -= 1
                
                if (nx, ny) not in visited:
                    heappush(heap, (cost + nw, nx, ny))
                    
        return -1
                
            
            