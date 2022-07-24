class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        for rows in matrix:
            if target < rows[0]:
                return False
            elif target > rows[-1]:
                continue
            else:
                left, right = 0, col -1
                if target == rows[left] or target == rows[right]:
                    return True
                while left < right:
                    mid = (left + right)//2
                    m = rows[mid]
                    if m == target:
                        return True
                    elif m < target:
                        left = mid + 1
                    else:
                        right = mid
                if rows[left] == target:
                    return True
        return False