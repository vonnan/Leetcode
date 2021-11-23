class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        
        if not nums:
            return 0
        
        diff = [0] + [nums[i] - nums[i-1] for i in range(1, n)]
        
        res = 1
        for i, val in enumerate(diff[1:],1):
            if (val < 0 and diff[i-1] >= 0) or (val > 0 and diff[i-1] <= 0):
                res += 1
            if val == 0:
                diff[i] = diff[i-1]
        return res
            