from bisect import insort
from bisect import bisect_left
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        lst = [nums[0]]
        res = -1
        
        for num in nums[1:]:
            idx = bisect_left(lst, k - num)
            if idx != 0:
                res = max(res, num + lst[idx -1])
            insort(lst, num)
        return res