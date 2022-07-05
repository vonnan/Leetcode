class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        
        nums = sorted(list(set(nums)))
        
        res = 1
        ct , start = 1, 0
        for i, num in enumerate(nums[1:],1):
            if num == nums[i-1] + 1:
                ct += 1
            else:
                res = max(res, ct)
                ct = 1
        return max(res, ct)
            
        
        