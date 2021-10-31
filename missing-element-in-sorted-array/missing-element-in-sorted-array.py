from bisect import bisect
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        first = nums[0]
        lst = [num - first - i for i, num in enumerate(nums)]
        idx = bisect_left(lst, k) - 1
        if idx < len(nums):
            return nums[idx] - lst[idx] + k
        else:
            return k -lst[-1] + nums[-1]
          
            