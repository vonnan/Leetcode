class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        
        prev, curr = 0 , 0
        for num in nums[1:]:
            prev, curr = curr, max(curr, prev + num)
        res = curr
        
        prev, curr = 0 , 0
        for num in nums[:-1]:
            prev, curr = curr, max(curr, prev + num)
        return max(res, curr)
            
        
            
            