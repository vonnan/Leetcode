class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum = [0]
        min_, res  = 0,  nums[0]
        for num in nums:
            last = presum[-1] + num
            presum.append(last)
            res = max(res, last - min_)
            min_ = min(min_, last)
        return res
            