class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums), set([])
        
        nums.sort()
        def dfs(nums, path):
            if len(path) == n:
                    res.add(tuple(path))
                    return
                
            for i, num in enumerate(nums):
                if i > 0 and num == nums[i-1]:
                    continue
                dfs(nums[:i] + nums[i+1:], path + [num])
        
        dfs(nums, [])
        return res
            
            
            