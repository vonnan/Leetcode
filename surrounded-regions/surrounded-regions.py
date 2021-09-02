class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = len(board), len(board[0])
        queue =deque([(r, c) for r in range(row) for c in range(col) if (r== 0 or r == row -1 or c == 0 or c == col -1 ) and board[r][c] == "O"])
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set(queue)
        
        while queue:
            m = len(queue)
            for _ in range(m):
                r,c = queue.popleft()
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    if (nr, nc ) not in visited:
                        if 0 <= nr <row and 0 <= nc < col and board[nr][nc] == "O":
                            visited.add((nr, nc))
                            queue.append((nr, nc))
        
        for r,c in visited:
            board[r][c] = "N"
         
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "N":
                    board[r][c] = "O"
        
        
            
        