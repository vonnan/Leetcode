class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)
        def check(x):
            ct, res = 0, 1
            for w in weights:
                if ct + w <= x:
                    ct += w
                else:
                    ct = w
                    res += 1
                    if res > days:
                        return False
            return True
                        
        while lo < hi:
            mid = (lo + hi)//2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
                