class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, board = [], []
        
        col, diag, off_diag = set(), set(), set()
        
        def dfs(r):
            if r == n:
                res.append(list(board))
                
            for c in range(n):
                if c not in col and r+ c not in off_diag and r-c not in diag:
                    col.add(c)
                    off_diag.add(r+c)
                    diag.add(r -c)
                    board.append("."*c + "Q" + "."*(n-1-c))
                    dfs(r + 1)
                    board.pop()
                    col.remove(c)
                    off_diag.remove(r+c)
                    diag.remove(r - c)
         
        dfs(0)
        
        return res
                    