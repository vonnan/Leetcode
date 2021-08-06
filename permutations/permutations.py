class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = set([]), len(nums)
        
        def dfs(nums, path):
            if len(path) == n:
                res.add(tuple(path))
                return
            
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])
                
        dfs(nums, [])
        
        return res
            
            