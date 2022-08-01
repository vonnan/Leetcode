from bisect import bisect_left
from bisect import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        elif target == matrix[0][0] or target == matrix[-1][-1]:
            return True
        
        row, col = len(matrix), len(matrix[0])
        
        lst =[rows[0] for rows in matrix]
        idx = bisect(lst, target)
        
        rows = matrix[idx -1]
        c = bisect_left(rows, target)
        if c != col and rows[c] == target:
            return True
        
        return False
                
        
        
        
    
                    
                