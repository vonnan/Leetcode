from bisect import bisect 
from bisect import bisect_left

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        presum = [0]
        for num in nums:
            presum.append(num + presum[-1])
        
        tot = presum[-1]
        target = tot//3
        idx = bisect(presum, target)
        #print(presum, idx)
        res = 0
        for i in range(1, idx):
            first = presum[i]
            idx_l = max(bisect_left(presum, 2 * first), i + 1)
            idx_r = min(len(nums), bisect(presum, (tot + first)//2))
            #print(idx, i, idx_l, idx_r)
            res += max(idx_r  - idx_l, 0)
            
        return res % (10**9 + 7)
            