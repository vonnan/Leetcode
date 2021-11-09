class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        res = [1]
        for num in nums[:-1]:
            p *= num
            res.append(p)
        
        p = 1
        n = len(nums)
        for i in range(n-1, 0, -1):
            p *= nums[i]
            res[i-1] *= p
        return res
            
