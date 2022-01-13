class Solution(object):
    def makesquare(self, nums):
        
        target, r = divmod(sum(nums), 4)
        nums.sort(reverse = 1)
        n = len(nums)
        if r or nums[0] > target:
            return False
       
        
        @lru_cache(None)
        def dfs(mask):
            if mask == 0: return 0
            
            for i in range(n):
                if mask & (1 << i):
                    nxt = dfs(mask ^ ( 1 << i))
                    if nxt >= 0 and (nxt + nums[i] <= target):
                        return (nxt + nums[i]) % target
                  
            return -1
        
        return dfs((1<<n)-1) == 0
                        
    
