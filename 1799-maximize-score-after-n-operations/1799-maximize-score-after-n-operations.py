from math import gcd
from itertools import combinations

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        
        gcds = {(i, j): gcd(nums[i], nums[j]) for (i,j) in combinations(range(n), 2)}
        
        @lru_cache(None)
        def dp(mask):
            if mask == 0:
                return 0
            
            res = 0
            
            not_assigned =[i for i in range(n) if mask &( 1<<i)]
            
            for j, k in combinations(not_assigned, 2):
                mask_nxt = mask ^ (1<<j) ^( 1 <<k)
                res = max(res, dp(mask_nxt) + (n - len(not_assigned) + 2)//2 * gcds[j,k])
            return res
        
        return dp((1<<n) - 1)