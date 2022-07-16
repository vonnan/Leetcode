from bisect import bisect

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right)//2
            ct = 0
            for i, num in enumerate(nums):
                idx = bisect(nums, num + mid)
                ct += idx - i - 1
                
                if ct > k:
                    
                    break
            
            if ct < k:
                left = mid + 1
            else:
                right = mid
        return left
            