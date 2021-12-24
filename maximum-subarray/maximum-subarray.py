class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_ = 0
        presum = [0]
        res = -inf
        for num in nums:
            nxt = presum[-1] + num
            presum.append(nxt)
            res = max(res, nxt - min_)
            min_ = min(min_, nxt)
        return res