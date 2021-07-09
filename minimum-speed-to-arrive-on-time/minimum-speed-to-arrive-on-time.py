from math import ceil

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1
        
        def check(m):
            res = 0
            for d in dist[:-1]:
                res += ceil(d/m)
            res += dist[-1]/m
            print(mid, res)
            return res <= hour
        
        left, right = 1, 10**7
        while left < right:
            mid = (left + right)//2
            if check(mid):
                right = mid
            else:
                left = mid + 1
                
        return right
            