class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        res, mod = 0, 10**9 + 7
        left = []
        
        for i, num in enumerate(nums + [0]):
            start_idx = i
            while left and left[-1][0] >= num:
                prev, start_idx = left.pop()
                res = max(res, (presum[i] - presum[start_idx])*prev)
            left.append((num, start_idx))
            
        return res % mod