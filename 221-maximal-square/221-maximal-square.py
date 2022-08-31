class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        res = 0
        for r in range(row):
            for c in range(col):
                matrix[r][c] = int(matrix[r][c])
            matrix[r] = [0] + matrix[r]
        
        matrix = [[0]*(col + 1)] + matrix
        
        
        for r in range(row):
            for c in range(col):
                if matrix[r+ 1][c+1]:
                    matrix[r + 1][c + 1] = min(matrix[r][c], matrix[r][c+1], matrix[r+1][c]) + 1
                    res = max(res, matrix[r + 1][c+ 1])
        
        return res * res
                