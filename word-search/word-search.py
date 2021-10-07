class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(idx,r,c):
            if self.found:
                return
            
            if idx == k:
                self.found = True
                return
            
            if 0 <= r < row and 0 <= c < col and board[r][c] ==word[idx]:
                if idx == k-1:
                    self.found = True
                    return
                
                tmp = board[r][c]
                board[r][c] = "*"
                for dr, dc in path:
                    dfs(idx + 1, r + dr, c + dc)
                
                board[r][c] = tmp
                
            else:
                return
            
        self.found = False
        
        row, col, k = len(board), len(board[0]), len(word)
        path = [(0,1), (0, -1), (1, 0), (-1, 0)]
        
        for r in range(row):
            for c in range(col):
                if self.found:
                    return True
                dfs(0, r, c)
        return self.found
                
        