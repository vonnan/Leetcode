from bisect import bisect
from bisect import bisect_left

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n, tot = len(nums), sum(nums)
        res, mod = 0, 10**9 + 7
        presum = [0]
        for num in nums:
            presum.append(num + presum[-1])
        print(presum)    
        for i, x in enumerate(presum[1:], 1):
            if 3*x > tot:
                break
                
            left = max(i + 1, bisect_left(presum, 2*x))
            right = min(bisect(presum, (tot + x)//2), n)
            
            print(x, left, right)
            res += max(0, right - left)
            
        return res % mod
            
        
            
        