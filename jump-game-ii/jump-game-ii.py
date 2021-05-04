class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)-1
        count = 0
        
        while n >0:
            for last in range(n):
                if last + nums[last] >= n:
                    break
            count += 1
            n = last
            
        return count 
            
        