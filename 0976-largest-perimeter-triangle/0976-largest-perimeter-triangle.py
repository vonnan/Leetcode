class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums) >= 3:
            if nums[-1] >= nums[-2] + nums[-3]:
                nums.pop()
            else:
                return sum(nums[-3:])
        
        if len(nums) < 3:
            return 0
        
        