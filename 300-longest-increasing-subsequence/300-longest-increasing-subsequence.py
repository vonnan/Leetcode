from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []
        for num in nums:
            idx = bisect_left(LIS, num)
            if idx == len(LIS):
                LIS.append(num)
            else:
                LIS[idx] = num
        return len(LIS)