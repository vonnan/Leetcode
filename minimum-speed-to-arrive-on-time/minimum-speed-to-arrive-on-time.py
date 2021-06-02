from math import ceil
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n-1:
            return -1
        
        left, right = 1, dist[-1]* 100
        
        while left < right:
            mid = (left + right)//2
            res = 0
            for i, d in enumerate(dist):
                if i != n-1:
                    res += ceil(d/mid)
                else:
                    res += d/mid
                if res > hour:
                    left = mid + 1
                    break
            if res <= hour:
                right = mid
        
        return left