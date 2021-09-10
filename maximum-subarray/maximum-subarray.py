class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum = [0]
        res, min_sofar = -inf, 0
        for num in nums:
            x = num + presum[-1]
            res = max(res, x - min_sofar)
            min_sofar = min(min_sofar, x)
            presum.append(x)
        return res