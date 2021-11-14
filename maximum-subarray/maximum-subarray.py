class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_, res = 0, nums[0]
        presum = [0]
        for num in nums:
            nxt = presum[-1] + num
            res = max(res, nxt - min_)
            min_ = min(min_, nxt)
            presum.append(nxt)
        return res
            