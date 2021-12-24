class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev, curr = 0, 0
        
        for num in nums[:-1]:
            prev, curr = curr, max(prev + num, curr)
        
        res = curr
        
        prev, curr = 0, 0
        for num in nums[len(nums) - 1:0:-1]:
            prev, curr = curr, max(prev + num, curr)
            
        return max(res, curr)