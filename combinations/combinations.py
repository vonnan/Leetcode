class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = set([])
        
        nums = list(range(1, n+1))
        
        def dfs(nums, path):
            if len(path) > k:
                return
            
            if len(path) == k:
                res.add(tuple(path))
                
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]])
                
        dfs(nums, [])
        
        return res