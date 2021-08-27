class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i, num in enumerate(nums[1:], 1):
            nums[i] += max(nums[i-1], 0)
            
        return max(nums)
            