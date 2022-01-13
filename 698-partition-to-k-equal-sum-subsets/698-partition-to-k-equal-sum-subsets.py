class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n, tot = len(nums), sum(nums)
        nums.sort(reverse = 1)
        
        if n < k or tot % k:
            return False
        
        target = tot//k
        
        @lru_cache(None)
        def dfs(mask):
            if mask == 0:
                return 0
            
            for i in range(n):
                if mask & (1<< i):
                    nxt = dfs(mask ^ (1 << i))
                    if nxt >= 0 and (nxt + nums[i] <= target):
                        return (nxt + nums[i]) % target
            return -1
        
        return dfs((1<<n)-1) == 0
