from bisect import bisect
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l,r = matrix[0][0], matrix[-1][-1]
        
        while l < r:
            mid = (l + r)//2
            tot = sum(bisect(row, mid) for row in matrix)
            if tot < k:
                l = mid + 1
            else:
                r = mid
        return l
        