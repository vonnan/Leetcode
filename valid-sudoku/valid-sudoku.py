class Solution:
    def isValidSudoku(self, A: List[List[str]]) -> bool:
        row, col, block = set([]), set([]), set([])
        
        for i in range(9):
            for j in range(9):
                if A[i][j] != ".":
                    r = (i, A[i][j])
                    c = (j, A[i][j])
                    b = (i//3, j//3, A[i][j])
                    if r in row or c in col or b in block:
                        return False
                    else:
                        row.add(r)
                        col.add(c)
                        block.add(b)
    
        return True