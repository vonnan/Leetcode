class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res, board =[], []
        cols, diag, off_diag = set(), set(), set()
        def dfs(r):
            if r == n:
                res.append(list(board))
            for c in range(n):
                if c not in cols and r - c not in diag and r+c not in off_diag:
                    cols.add(c)
                    diag.add(r-c)
                    off_diag.add(r+c)
                    board.append("."*c + "Q" + "."*(n-1-c))
                    dfs(r + 1)
                    board.pop()
                    off_diag.remove(r + c)
                    diag.remove(r - c)
                    cols.remove(c)
        dfs(0)
        return res
                    
                    
            
            