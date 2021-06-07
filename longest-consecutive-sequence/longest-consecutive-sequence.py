class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        nums = sorted(list(set(nums)))
        res = 1
        
        i, j = 0, 1
        
        while j < len(nums):
            while j < len(nums) and nums[j] == nums[j-1] + 1:
                j += 1
            res = max(res, j-i)
            i = j
            j = j + 1
        
        return res