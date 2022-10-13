class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums = sorted([key for key, val in counter.items() if val == 1])
        return nums[-1] if nums else -1