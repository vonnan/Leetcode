from bisect import bisect
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        weight = list(accumulate(weight))
        idx = bisect(weight, 5000)
        return idx
        