from math import gcd
from itertools import combinations

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        gcds = {(i, j): gcd(nums[i], nums[j]) for (i,j) in combinations(range(n), 2)}
        
        @lru_cache(None)
        def dfs(mask):
            if mask == 0 :
                return 0
            
            no_group = [i for i in range(n) if mask & (1 << i)]
            res = 0
            
            for i, j in combinations(no_group, 2):
                mask_nxt = mask ^ (1 <<i) ^ (1 <<j)
                res = max(res, dfs(mask_nxt) + (n - len(no_group) + 2)//2 * gcds[i, j])
            
            return res
        
        return dfs((1 << n) - 1)
                