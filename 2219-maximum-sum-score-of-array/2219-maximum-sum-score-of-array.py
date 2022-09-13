class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        tot = sum(nums)
        res = tot
        presum, suff = 0, tot
        
        for i, num in enumerate(nums):
            presum += num
            res = max([res, presum, suff])
            suff -= num
        return res
            
        