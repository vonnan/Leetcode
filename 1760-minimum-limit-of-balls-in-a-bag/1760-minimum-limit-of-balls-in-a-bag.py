from math import ceil
class Solution:
    def minimumSize(self, nums: List[int], max_: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right)//2
            tot = sum(ceil(num/mid) - 1 for num in nums if num > mid)
            if tot > max_:
                left = mid + 1
            else:
                right = mid
        return left