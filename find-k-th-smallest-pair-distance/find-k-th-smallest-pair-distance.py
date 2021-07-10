from bisect import bisect
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            mid = (l + r)//2
            if sum(bisect(nums, nums[i] + mid) - (i+1) for i in range(len(nums))) >= k:
                r = mid
            else:
                l = mid + 1
        return l
                
            