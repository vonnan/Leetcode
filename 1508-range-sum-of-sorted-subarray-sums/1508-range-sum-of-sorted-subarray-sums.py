
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res, mod = [], 10 ** 9 + 7
        
        for i in range(n):
            tot = 0
            
            for j in range(i, n):
                tot += nums[j]
                res.append(tot)
        
        return sum(sorted(res)[left-1: right])%mod