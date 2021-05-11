import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        
        if set(nums) == {0}:
            return "0"
        
        nums = sorted([str(num) for num in nums], reverse = 1)
        
        def compare(a, b):
            if int(a +b) > int(b+a):
                return True
            else: 
                return False
        
        n = len(nums)    
        for i in range(n):
            for j in range(i, n):
                if not compare(nums[i], nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        
        return "".join(nums)
        