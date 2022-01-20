class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n, tot = len(nums), sum(nums)
        if tot %k:
            return False
        
        nums.sort(reverse = 1)
        
        target = tot//k
        
        @lru_cache(None)
        def helper(mask, side, t):
            if mask == 0 and side == 0:
                return True
            
            for i in range(n):
                if mask & ( 1<< i):
                    
                    if nums[i] > t:
                        break
                    mask_nxt = mask ^ (1 <<i)
                    if nums[i] == t:
                        if helper(mask_nxt, side -1, target):
                            return True
                    else:
                        if helper(mask_nxt, side, t - nums[i]):
                            return True
            return False
        
        return helper((1<<n)-1, k, target)
                        