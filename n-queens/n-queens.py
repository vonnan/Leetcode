class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, diag, off_d = set([]), set([]), set([])
        board, res = [], []
        
        def dfs(r):
            if r == n:
                res.append(board[:])
            
            else:
                for c in range(n):
                    if c not in col and (r-c not in diag) and (r + c not in off_d):
                        col.add(c)
                        diag.add(r - c)
                        off_d.add(r + c)
                        board.append(c * "." + "Q" + (n-1-c) * ".")
                        dfs(r + 1)
                        board.pop()
                        col.remove(c)
                        diag.remove(r-c)
                        off_d.remove(r+c)
        
        dfs(0)
        return res
                        