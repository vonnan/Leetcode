class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        back = nums[::-1]
        
        for i, num in enumerate(nums[1:], 1):
            nums[i] *= nums[i-1] or 1
            back[i] *= back[i-1] or 1
            
        return max(max(nums), max(back))