class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_ = 0
        presum = [0]
        res = -inf
        for num in nums:
            nxt = presum[-1] + num
            res = max(res, nxt - min_)
            min_ = min(min_, nxt)
            presum.append(nxt)
        return res
        