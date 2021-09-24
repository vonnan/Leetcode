class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach =[i + num for i, num in enumerate(nums)]
        max_, n = reach[0], len(nums)
        if n ==1:
            return True
        
        i = 0
        while i< n:
            if nums[i] ==0 and max_ <=i:
                return False
            max_ = max(max_, max(reach[i+1: max_ + 1]))
            if max_ >= n-1:
                return True
            
            i += 1
            
                
            