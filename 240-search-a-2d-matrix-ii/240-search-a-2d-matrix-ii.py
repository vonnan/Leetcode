class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        for r in range(row):
            if target > matrix[r][-1]:
                continue
            else:
                if target in matrix[r]:
                    return True
        return False