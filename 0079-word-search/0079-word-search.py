class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(word)
        row, col = len(board), len(board[0])
        
        def dfs(pos, r, c, seen):
            if pos == n:
                return True
            
            for dr, dc in path:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and ((nr, nc) not in seen) and word[pos] == board[nr][nc]:
                    if dfs(pos + 1, nr, nc, seen | set([(nr, nc)])):
                        return True
            
            return False
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if dfs(1, r, c, set([(r, c)])):
                        return True
        return False