class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        prev, curr = 0, 0
        
        for i, num in enumerate(nums[:-1]):
            prev, curr = curr, max(curr, prev + num)
            
        res = curr
        
        prev, curr = 0, 0
        
        for i, num in enumerate(nums[1:], 1):
            prev, curr = curr, max(curr, prev + num)
            
        return max(res, curr)
