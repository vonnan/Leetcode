class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[]]
        for num in nums:
            dp.append(max([s + [num] for s in dp if not s or num%s[-1] ==0], key = len))
        return max(dp, key = len)
        