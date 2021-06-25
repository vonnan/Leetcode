class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        stack = []
        
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)
                
        for j in range(n-1,-1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                res = max(res, j - stack.pop())
                
        return res