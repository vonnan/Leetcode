from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        left, right = 1, nums[-1]
        
        while left < right:
            mid = (left + right)//2
            if sum(ceil(num/ mid) for num in nums) <= threshold:
                right = mid
            else:
                left = mid + 1
        return left