class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = set([]), len(nums)
        
        def dfs(nums, path):
            if len(path) ==n:
                res.add(tuple(path))
                
            for i, num in enumerate(nums):
                dfs(nums[:i] + nums[i + 1:], path + [num])
        
        dfs(nums, [])
        return res
        