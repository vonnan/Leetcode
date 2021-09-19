class Solution:
    def solve(self, A: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(A), len(A[0])
        q = deque([(r,c) for r in range(row) for c in range(col) if (r == 0 or r== row-1 or c == 0 or c == col - 1) and A[r][c] == "O"])
        path = [(1,0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            m = len(q)
            for _ in range(m):
                r,c = q.popleft()
                if A[r][c] == "O":
                    A[r][c] = "N"
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and A[nr][nc] == "O":
                        A[nr][nc] = "N"
                        q.append((nr, nc))
        
        for r in range(row):
            for c in range(col):
                if A[r][c] == "O":
                    A[r][c] = "X"
                if A[r][c] == "N":
                    A[r][c] = "O"
        
        return A
                        