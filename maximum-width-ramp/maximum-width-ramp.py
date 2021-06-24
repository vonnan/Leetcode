class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, num in enumerate(nums):
            if not stack or num < nums[stack[-1]]:
                stack.append(i)
                
        n, res, k = len(nums), 0, inf
        
        for j in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                k = stack.pop()
            res = max(res, j - k)
        
        return res
            
           
        
            