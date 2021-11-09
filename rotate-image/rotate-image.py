class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for r in range(n):
            matrix[r] = matrix[r][::-1]
            
        for r in range(n):
            for c in range(n - r):
                matrix[r][c], matrix[n - 1 - c][n - 1 - r] = matrix[n - 1 - c][n - 1 - r], matrix[r][c]
        