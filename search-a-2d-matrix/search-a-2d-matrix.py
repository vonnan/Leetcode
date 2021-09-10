class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        
        for r in matrix:
            if target < r[0]:
                return False
            if target > r[-1]:
                continue
            left, right = 0, col -1
            while left < right:
                mid = (left + right)//2
                if r[mid] == target:
                    return True
                if target > r[mid]:
                    left = mid + 1
                else:
                    right = mid
            if r[left]== target:
                return True
            else:
                return False
        return False