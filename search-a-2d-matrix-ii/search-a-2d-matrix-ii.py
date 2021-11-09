class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        for r in range(row):
            if target > matrix[r][-1]:
                continue
            
            left, right = 0, col - 1
            
            while left < right:
                mid = (left + right)//2
                if matrix[r][mid] == target:
                    return True
                if matrix[r][mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
            if target == matrix[r][left]:
                return True
        return False   
            
        