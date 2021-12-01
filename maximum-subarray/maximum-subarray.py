class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_ = 0
        presum = [0]
        res = -inf
        for num in nums:
            nxt = num + presum[-1]
            res = max(res, nxt - min_)
            presum.append(nxt)
            min_ = min(min_, nxt)
        return res
            