from math import ceil
class Solution:
    def minimumSize(self, nums: List[int], max_: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right)//2
            ct = 0
            for num in nums:
                if num > mid:
                    ct += ceil(num/mid) - 1
                    if ct > max_:
                        break
            
            if ct > max_:
                left = mid + 1
            else:
                right = mid
        return left