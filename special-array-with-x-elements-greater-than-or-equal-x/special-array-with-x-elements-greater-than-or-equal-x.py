from bisect import bisect_left
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if nums[0] >= n:
            return n

        for candidate in range(1, n+1):
            if nums[n-1-candidate] < candidate <= nums[n-candidate]:
                return candidate
            
        return -1
        