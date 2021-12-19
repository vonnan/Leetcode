from bisect import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        subs = [0]*(size)
        subs[0] = 1

        for i in range(1, size):
            maximum = 0
            for j in range(0, i):
                if nums[j] < nums[i] and maximum < subs[j]:
                    maximum = subs[j]
            subs[i] = maximum + 1
        return max(subs)        