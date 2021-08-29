class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #nums += [0]
        prev, curr = 0, 0
        
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        
        return curr