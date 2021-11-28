class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        prev, curr = 0, nums[0]
        for num in nums[1:-1]:
            prev, curr = curr, max(curr, prev + num)
        res = curr
        prev, curr = 0, nums[1]
        for num in nums[2:]:
            prev, curr = curr, max(curr, prev + num)
        return max(res, curr)
            