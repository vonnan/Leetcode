from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if sum(nums)<= threshold:
            return 1
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi)//2
            if sum(ceil(num/mid) for num in nums) <= threshold:
                hi = mid
            else:
                lo = mid + 1
        return lo
        