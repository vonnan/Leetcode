from math import gcd
from itertools import combinations

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        dic = {(i,j): gcd(nums[i], nums[j]) for (i,j) in combinations(range(n), 2)}
        
        @lru_cache(None)
        def dfs(mask):
            if mask == 0:
                return 0
            
            res = 0
            nbits =[i for i in range(n) if mask & (1 <<i)]
            
            for i,j in combinations(nbits, 2):
                q = mask ^ (1<<i) ^ (1 <<j)
                res = max(res, dfs(q) + (n - len(nbits) + 2)//2 * dic[i,j])
            
            return res
        
        return dfs((1 << n) - 1)
        
        
        
        
        
        
        