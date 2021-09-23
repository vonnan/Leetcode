class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        lst = [nums[i] - nums[i-1] for i in range(1, n)]
        res, ct = 0, 1
        for i, num in enumerate(lst[1:], 1):
            if num == lst[i-1]:
                ct += 1
                if i == n-2:
                    return res + ct*(ct-1)//2
            else:
                if ct >=2:
                    res += ct*(ct-1)//2
                    ct = 1
        return res            