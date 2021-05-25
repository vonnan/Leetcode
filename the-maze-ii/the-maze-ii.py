from collections import defaultdict
from heapq import heappush
from heapq import heappop
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        path = [(0,1), (0,-1), (1,0), (-1,0)]
        heap = [(0, start[0], start[1])]
        dist = {}
        
        while heap:
            w, x,y = heappop(heap)
            if (x,y) in dist:
                continue
            dist[(x,y)] = w
            if destination ==[x,y]:
                return w
            for dx, dy in path:
                nx, ny = x, y
                nw = 0
                while 0<= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                    nx += dx
                    ny += dy
                    nw += 1
                nx -= dx
                ny -= dy
                nw -= 1
                if (nx, ny) in dist:
                    continue
                heappush(heap, (w + nw, nx, ny))
                
        return -1
                    
                    