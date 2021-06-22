class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        def dfs(nums, ans):
            if len(ans) ==n:
                res.append(ans[:])
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], ans + [nums[i]])
                
                    
        dfs(nums, [])
        return res
    
        """
        n = len(nums)
        sol = [[nums[0]]]
        
        for i in range(1, n):
            new = []
            x = nums[i]
            for j in range(i+1):
                new.extend(y[:j] + [x] + y[j:] for y in sol)
                print(new, sol)
                
            sol = new
            
        return sol
            
        """
            

    