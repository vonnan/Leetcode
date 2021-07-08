from bisect import bisect
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        
        while left < right:
            mid = (left + right)//2
            if sum(bisect(row, mid) for row in matrix) < k:
                left = mid + 1
            else:
                right = mid
                
        return left