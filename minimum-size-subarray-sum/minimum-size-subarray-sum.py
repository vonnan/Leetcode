class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        
        res, j  = n + 1, 0
        
        for i in range(n):
            target -= nums[i]
            while target <= 0:
                res = min(res, (i - j + 1))
                target += nums[j]
                j += 1
                
        return res if res != n+1 else 0
            
                
                
                
                
            