class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        for r in matrix:
            if target < r[0]:
                return False
            elif target > r[-1]:
                continue
            else:
                return target in r