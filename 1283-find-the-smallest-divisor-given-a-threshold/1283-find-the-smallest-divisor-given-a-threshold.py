from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort(reverse = 1)
        left, right = 1, nums[0]
        
        while left < right:
            mid = (left + right)//2
            ct = 0
            for num in nums:
                ct += ceil(num/mid)
                if ct > threshold:
                    break
            if ct > threshold:
                left = mid + 1
            else:
                right = mid
        return left
            