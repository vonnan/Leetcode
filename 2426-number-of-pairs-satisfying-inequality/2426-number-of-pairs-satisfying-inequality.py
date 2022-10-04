from bisect import bisect
from bisect import insort

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = [a - b for a, b in zip(nums1, nums2)]
    
        lst = []
        res = 0
        for num in nums:
            idx = bisect(lst, num + diff)
            res += idx
            insort(lst, num)
        return res
            