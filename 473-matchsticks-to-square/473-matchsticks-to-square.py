class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        n, tot = len(nums), sum(nums)
        nums.sort(reverse = 1)
        target = tot//4
        if tot%4 or nums[0] > target:
            return False
        
        @lru_cache(None)
        def dfs(mask, sides, t):
            if mask == 0 and sides ==0:
                return True
            
            for i in range(n):
                if mask & (1 << i):
                    if t < nums[i]:
                        break
                    mask_ = mask ^(1 <<i)
                    if t == nums[i]:
                        if dfs(mask_, sides -1, target):
                            return True
                    elif dfs(mask_, sides, t - nums[i]):
                        return True
            
            return False
        
        return dfs((1<<n)-1, 4, target)