from bisect import bisect

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        n = len(matrix)
        while lo < hi:
            mid = (lo + hi)//2
            ct = sum(bisect(rows, mid) for rows in matrix)
            
            if ct < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
                