from bisect import bisect

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        left, right = matrix[0][0], matrix[-1][-1]
        
        while left < right:
            mid = (left + right)//2
            ct = 0
            for rows in matrix:
                ct += bisect(rows, mid)
                if ct > k:
                    right = mid
                    break
            
            if ct < k:
                left = mid + 1
            elif ct >= k:
                right = mid
        
        return left
                    
                    