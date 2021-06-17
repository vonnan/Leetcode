class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0
        
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)
                
        for i in range(len(nums)-1, -1, -1):
            j = i
            while stack and nums[stack[-1]] <= nums[i]:
                j = stack.pop()
            res = max(res, i - j)
        return res
            
        
            