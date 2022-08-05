class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        back = nums[::-1]
        
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            back[i] *= back[i - 1] or 1
        
        print(nums, back)
        return max(max(nums), max(back))