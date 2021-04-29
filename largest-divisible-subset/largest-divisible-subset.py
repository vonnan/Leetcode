class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [[]]
        for num in sorted(nums):
            dp.append(max((s + [num] for s in dp if not s or num% s[-1] == 0), key = len))
        return max(dp, key = len)