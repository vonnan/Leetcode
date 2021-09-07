class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = set([]), len(nums)
        
        def dfs(num, path):
            if len(path) == n:
                res.add(tuple(path))
            
            else:
                for i in range(len(num)):
                    dfs(num[:i] + num[i+1:], path + [num[i]])
        
        dfs(nums, [])
        
        return res