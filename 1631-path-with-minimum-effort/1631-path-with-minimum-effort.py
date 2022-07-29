class Solution:
    def minimumEffortPath(self, A: List[List[int]]) -> int:
        row, col = len(A), len(A[0])
        
        seen = set([])
        
        heap = [(0, 0, 0)]
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while heap:
            val, r, c = heappop(heap)
            if (r,c) in seen:
                continue
            else:
                seen.add((r, c))
            if r == row -1 and c == col - 1:
                return val
            prev = A[r][c]
            
            for dr, dc in path:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in seen:
                    nv = max(val, abs(A[nr][nc] - prev))
                    heappush(heap, (nv, nr, nc))