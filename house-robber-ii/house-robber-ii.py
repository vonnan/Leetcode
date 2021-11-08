class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev, curr = 0, nums[0]
        for num in nums[1:-1]:
            prev, curr = curr, max(prev + num, curr)
        
        res = curr
        prev, curr = 0, nums[1]
        for num in nums[2:]:
            prev, curr = curr, max(prev + num, curr)
        
        return max(res, curr)