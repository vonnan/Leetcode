class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res, left = 0, 0
        
        for right in range(n):
            k += nums[right]
            if k < nums[right] * (right - left + 1):
                k -= nums[left]
                left += 1

        return right - left + 1
            
                