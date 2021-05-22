class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(i):
            if i == n:
                res.append(list(board))
            for j in range(n):
                if j not in cols and j- i not in diag and j + i not in off_diag:
                    cols.add(j)
                    diag.add(j-i)
                    off_diag.add(j+i)
                    board.append("."* j + "Q" + "."* (n-1-j))
                    backtrack(i + 1)
                    board.pop()
                    off_diag.remove(j+i)
                    diag.remove(j-i)
                    cols.remove(j)
                    
        res, board = [], []
        
        cols, diag, off_diag = set(), set(), set()
        
        backtrack(0)
        
        return res
    
                    
            