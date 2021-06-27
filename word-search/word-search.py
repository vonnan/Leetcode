class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        seen = set()
        
        path = [(0,1), (0, -1), (1, 0), (-1,0)]
        
        def backtracking(r,c, ct):
            if ct == len(word):
                return True
            for dr, dc in path:
                nr, nc = r + dr, c + dc
                if 0 <=  nr <row and 0 <= nc < col and (nr, nc) not in seen and board[nr][nc] ==word[ct]:
                    seen.add((nr, nc))
                    if backtracking(nr, nc, ct + 1):
                        return True
                    seen.remove((nr, nc))
                    
        for r in range(row):
            for c in range(col):
                seen.add((r, c))
                if board[r][c] ==  word[0] and backtracking(r,c,1):
                    return True
                seen.remove((r,c))
        return False