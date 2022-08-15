from math import ceil

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        
        left, right = 1, 10 ** 7
        while left < right:
            mid = (left + right)//2
            hr = 0
            
            for d in dist[:-1]:
                hr += ceil(d/mid)
                if hr > hour:
                    break
            hr += dist[-1]/ mid
            
            if hr > hour:
                left = mid + 1
            else:
                right = mid
                
        return left
                