from bisect import bisect_left

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = [num for num in nums if num > 0]
        if len(nums) < 3:
            return 0
        
        n = len(nums)
        res = 0
        nums.sort()
        
        for i, ni in enumerate(nums[:-2]):
            for j, nj in enumerate(nums[i+1:-1], i + 1):
                idx = bisect_left(nums, ni + nj) - 1
                if idx > j:
                    res += idx - j
                
        
        return res
                