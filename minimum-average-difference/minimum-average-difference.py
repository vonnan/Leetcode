class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        right = sum(nums)
        n = len(nums)
        res = inf
        ans = 0
        left = 0
        
        for i, num in enumerate(nums):
            left += num
            right -= num
            
            if i == n-1:
                diff = sum(nums)//n
            else:
                diff = abs(left//(i + 1) - right//(n - 1 - i)) 
            
            if diff < res:
                res = diff
                ans = i 
            
        return ans