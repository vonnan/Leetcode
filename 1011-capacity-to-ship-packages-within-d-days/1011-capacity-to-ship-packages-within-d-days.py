class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right)//2
            ct = 0
            day = 1
            for w in weights:
                if ct + w > mid:
                    day += 1
                    ct = w
                    if day > days:
                        left = mid + 1
                        break
                else:
                    ct += w
            if day > days:
                left = mid + 1
            else:
                right = mid
            
        
        return left