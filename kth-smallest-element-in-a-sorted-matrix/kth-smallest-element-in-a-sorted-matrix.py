from bisect import bisect
class Solution:
    def kthSmallest(self, A: List[List[int]], k: int) -> int:
        lo, hi = A[0][0], A[-1][-1]
        while lo < hi:
            mid = (lo + hi)//2
            if sum(bisect(row, mid) for row in A) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
            