class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n, tot = len(nums), sum(nums)
        nums.sort(reverse = 1)
        
        if n < k or tot % k:
            return False
        
        target = tot//k
        
        t = [target] * k
        
        def dfs(pos):
            if pos == n:
                return True
            
            for i in range(k):
                if t[i] >= nums[pos]:
                    t[i] -= nums[pos]
                    if dfs(pos+1):
                        return True
                    t[i] += nums[pos]
            return False
        
        return dfs(0)