class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n -1
        
        res = 0
        while left < right:
            l, r = height[left], height[right]
            res = max(res, min(l, r) * (right - left))
            if l <= r:
                left += 1
            else:
                right -= 1
        return res