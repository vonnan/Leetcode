class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        left, res, product = 0, 0, 1
        
        for right in range(n):
            product *= nums[right]
            
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            
            res += right - left + 1
            
        return res
        
        