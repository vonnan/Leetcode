class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))
        res = set([])
        
        def dfs(nums, path, n):
            if len(path) == k and not n:
                res.add(tuple(path))
            
            for i, num in enumerate(nums):
                if path and num < path[-1]:
                    continue
                    
                if num > n:
                    break
                
                dfs(nums[:i] + nums[i+1:], path + [num], n - num)
        
        dfs(nums, [], n)
        return res