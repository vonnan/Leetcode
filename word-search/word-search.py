class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(idx , r, c):
            
            if idx == k:
                self.status = True
                
            if self.status:
                return
            
            if 0 <= r < row and 0 <= c <col and board[r][c] == word[idx]:
                temp = board[r][c]
                board[r][c] = "*"
                for dr, dc in path:
                    dfs(idx + 1, r + dr, c + dc)
                board[r][c] = temp
                
            else:
                return
            
        self.status = False
        row, col, k = len(board), len(board[0]), len(word)
        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for r in range(row):
            for c in range(col):
                if self.status:
                    return True
                dfs(0, r, c)
        return self.status
                