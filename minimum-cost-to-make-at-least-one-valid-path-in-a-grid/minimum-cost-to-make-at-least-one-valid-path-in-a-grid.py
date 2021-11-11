class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        moves = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        heap = [(0, 0, 0)]
        visited = set()
        row, col = len(grid), len(grid[0])
        
        while heap:
            cost, r, c = heappop(heap)
            if r == row-1 and c == col-1:
                return cost
            
            if (r,c) in visited:
                continue
            visited.add((r,c))
            
            for move in moves:
                dr, dc = moves[move]
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited:
                    continue
                if 0 <= nr < row and 0 <= nc < col:
                    heappush(heap, (cost + (move != grid[r][c]), nr, nc))