from sortedcontainers import SortedList

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        presum = list(accumulate(nums, initial = 0))
        SL = SortedList([])
        for i in range(n):
            for j in range(i + 1, n + 1):
                SL.add(presum[j] - presum[i])
        return sum(SL[left - 1:right]) %(10**9 + 7)
        