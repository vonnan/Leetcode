class Solution(object):
    def makesquare(self, nums):
        if not nums:
            return False
        
        tot = sum(nums)
        nums.sort(reverse = 1)
        
        target, n = tot//4, len(nums)
        
        if tot % 4 or nums[0] > target:
            return False
         
        def helper(mask, sides, t):
            if sides == 0 and mask == 0:
                return True
            
            for i in range(n):
                if mask & (1 << i):
                 
                    if nums[i] > t:
                        #print(i, t, nums[i])
                        break
                    
                    elif nums[i] == t:
                        #print(i, t, nums[i], mask ^ (1 <<i), sides - 1, target)
                        if helper(mask ^ (1 <<i), sides - 1, target):
                            return True
                    elif nums[i] < t:
                        #print(i, t, nums[i], mask ^ (1 <<i), sides - 1, target)
                        if helper(mask ^ (1 <<i), sides, t - nums[i]):
                            return True
            return False
        
        return helper((1<<n)-1, 4, target)
                        
    
