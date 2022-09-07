
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        piles.sort(reverse= 1)
        
        while left < right:
            mid =  (left + right)//2
            t = 0
            for p in piles:
                t += ceil(p/mid)
                if t > h:
                    break
            if t <= h:
                right = mid
            else:
                left = mid + 1
                
        return left
                
                
            