class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set([])
        
        def dfs(nums, prev):
            if nums:
                for i, num in enumerate(nums):
                    if not prev or num >= prev[-1]:
                        if prev:
                            res.add(tuple(prev + [num]))
                        dfs(nums[i + 1:], prev + [num])
        
        dfs(nums, [])
        return res
                    