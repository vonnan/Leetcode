class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum = [0]
        min_ = 0
        res = -inf
        
        for num in nums:
            nxt = num + presum[-1]
            res = max(res, nxt - min_)
            min_ = min(min_, nxt)
            presum.append(nxt)
        
        return res