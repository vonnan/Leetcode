class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, res  = 0, 0
        for right, num in enumerate(nums):
            k -= 1 - num
            if k < 0:
                k += 1 - nums[left]
                left += 1
            
        return right - left + 1
            
                
            
        