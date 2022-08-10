class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        
        res = set([])
        
        def dfs(visited, path):
            if len(visited) == n:
                res.add(tuple(path))
            
            for i, num in enumerate(nums):
                if i not in visited:
                    dfs(visited | set([i]), path + [num])
    
        dfs(set([]), [])
        return res
                