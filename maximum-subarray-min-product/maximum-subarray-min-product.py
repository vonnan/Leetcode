class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        presum = [0]
        for num in nums:
            presum.append(num + presum[-1])
            
        n, mod = len(nums), 10**9 + 7
        left = []
        res = 0
        
        for i, num in enumerate(nums + [0]):
            j = i
            while left and left[-1][1] >= num:
                j, m = left.pop()
                res = max(res, (presum[i] - presum[j])*m )
            left.append((j, num))
            
        return res % mod
            