class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        return len(set(nums)) == n and nums[-1] - nums[0] == n-1