from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1 , sum(piles)
        while left < right:
            mid = (left + right)//2
            ct = 0
            for pile in piles:
                ct += ceil(pile/mid)
                if ct > h:
                    break
            
            if ct > h:
                left = mid + 1
            else:
                right = mid
        
        return left
                