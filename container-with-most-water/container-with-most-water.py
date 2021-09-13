class Solution:
    def maxArea(self, height: List[int]) -> int:
        n, res = len(height), 0
        left, right = 0, n-1
        while left< right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
                