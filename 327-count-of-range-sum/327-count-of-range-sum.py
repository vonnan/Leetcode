from sortedcontainers import SortedList
from bisect import bisect_left
from bisect import bisect

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = SortedList([0])
        prev = 0
        res = 0
        for num in nums:
            
            nxt = prev + num
            left, right = presum.bisect_left(nxt - upper), presum.bisect(nxt- lower)
            #print(num, nxt, nxt- upper, nxt- lower, left, right, presum)
            res += right - left
            presum.add(nxt)
            prev = nxt
        
        return res
            
            