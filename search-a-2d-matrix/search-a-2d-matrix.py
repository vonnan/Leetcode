class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        r= 0
        
        while r < row:
            if matrix[r][-1] < target:
                r += 1
            else:
                return target in matrix[r]
            
        return False
    
                    
                