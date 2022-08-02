from sortedcontainers import SortedList
from bisect import bisect_left
from bisect import bisect

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        s, total, res = SortedList([0]), 0, 0
        for n in nums:
            total +=n
            res += s.bisect_right(total-lower) - s.bisect_left(total-upper)
            s.add(total)
        return res
            
            