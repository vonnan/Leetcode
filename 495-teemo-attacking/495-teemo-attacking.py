from bisect import bisect_left

class Solution:
    def findPoisonedDuration(self, times: List[int], d: int) -> int:
        res = d
        
        for i, t in enumerate(times[:-1]):
            if t + d <= times[i+1]:
                res += d
            else:
                res += times[i+1] - t
        
        return res
            