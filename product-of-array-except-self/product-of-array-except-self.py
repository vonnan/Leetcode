class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 1, 1
        res =[1] * n
        
        for i in range(n):
            res[i] *= l
            l = l * nums[i]
            res[~i] *= r
            r = r * nums[~i]
        return res