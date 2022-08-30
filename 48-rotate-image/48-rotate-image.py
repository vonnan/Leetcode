class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        
        for r in range(row//2):
            matrix[r], matrix[row - 1 - r] = matrix[row - 1 -r], matrix[r]
        print(matrix)    
        for r in range(row):
            for c in range(r, col):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                
        return matrix
            