class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += max(nums[i-1], 0)
        return max(nums)
            