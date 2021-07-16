from bisect import bisect
class Solution:
    def findKthNumber(self, m, n, k):
        def enough(x):
            return sum(min(x // i, n) for i in range(1, m+1)) >= k

        lo, hi = 1, m*n
        while lo < hi:
            mi = (lo + hi) // 2
            if not enough(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo