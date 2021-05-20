from bisect import bisect_left
from bisect import insort
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        sort_lst = []
        for i in range(len(nums)-1, -1, -1):
            idx = bisect_left(sort_lst, nums[i])
            res.append(idx)
            insort(sort_lst, nums[i])
        return res[::-1]