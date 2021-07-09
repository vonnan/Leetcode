class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if sum(ribbons) < k:
            return 0
        
        ribbons.sort(reverse = 1)
        
        limit = ribbons[0]
        left, right = 0, limit
        
        while left < right:
            mid = (left + right + 1)//2
            ct = 0
            for ribbon in ribbons:
                ct += ribbon // mid
            if ct < k:
                right = mid -1
            else:
                left = mid
        return left