class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [[num] + p 
                for i, num in enumerate(nums) 
                for p in self.permute(nums[:i] + nums[i+1:])] or [[]]