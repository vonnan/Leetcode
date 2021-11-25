class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums =sorted([num for num in nums if num <= target])
        if not nums:
            return 0
        
        @lru_cache(None)
        def dfs(remain):
            if remain == 0:
                return 1
            
            res = 0
            for num in nums:
                if num <=remain:
                    res += dfs(remain - num)
                else:
                    break
            return res
        
        return dfs(target)
                    
