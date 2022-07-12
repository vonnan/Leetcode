class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left, right = 1, max(ribbons)
        if sum(ribbons) < k:
            return 0
        elif sum(x//right for x in ribbons) >= k:
            return right
        
        while left < right:
            mid = (left + right + 1)//2
            ct = sum(x//mid for x in ribbons)
            if ct < k:
                right = mid - 1
            else:
                left = mid 
        return left