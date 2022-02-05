class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n, tot = len(nums), sum(nums)
        
        if tot % k:
            return False
        
        target = tot//k
        nums.sort(reverse = 1)
        
        @lru_cache(None)
        def helper(mask, side, t):
            if side == 0 and mask == 0:
                return True
            
            for i in range(n):

                if mask & (1<<i):
                    if nums[i] >t:
                        break
                    if t == nums[i]:
                        if helper(mask ^(1<<i), side -1, target):
                            return True
                    else:
                        if helper(mask^(1<<i), side, t - nums[i]):
                            return True
            
            return False
        
        return helper((1<<n)-1, k, target)