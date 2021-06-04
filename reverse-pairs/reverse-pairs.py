from bisect import bisect
from bisect import insort
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        lst = []
        res = 0
        for num in nums:
            res += len(lst) - bisect(lst, num)
            insort(lst, num/2)
        return res
            