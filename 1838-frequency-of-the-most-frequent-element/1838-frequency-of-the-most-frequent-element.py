class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, left = 1, 0
        
        for right in range(len(nums)):
            if k < nums[right] * (right - left):
                k -= nums[left]
                left += 1
            k += nums[right]
        return right - left + 1
            
        
         