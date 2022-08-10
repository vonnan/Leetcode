from bisect import bisect_left
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                idx = bisect_left(nums, nums[i] + nums[j]) -1
                if idx > j:
                    res += idx - j
        return res
                
        