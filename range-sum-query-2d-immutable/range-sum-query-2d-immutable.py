class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.grid = [[0] * (col + 1) for _ in range(row + 1)]
        for r in range(row):
            for c in range(col):
                self.grid[r+1][c+1] = matrix[r][c] + self.grid[r+1][c] + self.grid[r][c+1] - self.grid[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.grid[row2 + 1][col2+1] + self.grid[row1][col1] - self.grid[row1][col2+1] - self.grid[row2 + 1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)