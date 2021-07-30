class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n, tot = len(nums), sum(nums)
        target = tot // k
        
        nums.sort(reverse = 1)
        
        if tot % k:
            return False
        
        target = [ tot//k] * k
        
        def dfs(pos):
            if pos == n:
                return True
            
            for i in range(k):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    
                    if dfs(pos + 1):
                        return True
                    target[i] += nums[pos]
                    
            return False
        
        return dfs(0)
            
            
        
        
        