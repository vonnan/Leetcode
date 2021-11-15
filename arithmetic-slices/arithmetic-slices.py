class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        lst = [nums[i] - nums[i-1] for i in range(1,n)]
        
        n -= 1
        
        ct, res = 1, 0
        for i, num in enumerate(lst[1:], 1):
            if num == lst[i -1]:
                ct += 1
                if i == n-1:
                    res += ct * (ct -1)//2
            else:
                res += ct * (ct -1)//2
                ct = 1
        return res
        
                
        