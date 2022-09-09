class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, block = defaultdict(set), defaultdict(set), defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                
                if board[r][c] != ".":
                    num = board[r][c]
                    if num in row[r] or (num in col[c]) or (num in block[(r//3, c//3)]):
                        return False
                    else:
                        row[r].add(num)
                        col[c].add(num)
                        block[(r//3, c//3)].add(num)
        
        return True