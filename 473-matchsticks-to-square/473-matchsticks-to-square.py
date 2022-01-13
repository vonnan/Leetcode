class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        n, tot = len(nums), sum(nums)
        nums.sort(reverse = 1)
        
        target = tot//4
        
        if tot % 4 or nums[0] > target or n < 4:
            return False
        
        t = [target] * 4
        
        #@lru_cache(None)
        def dfs(pos):
            if pos == n:
                return True
            
            for i in range(4):
                if t[i] >= nums[pos]:
                    t[i] -= nums[pos] 
                    if dfs(pos + 1):
                        return True
                    t[i] += nums[pos]
            return False
        
        return dfs(0)
                    