class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i, num in enumerate(nums):
            if i >= 1:
                res = max(res, num - nums[i-1])
        return res
            