class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, prev):
            if nums:
                for i in range(len(nums)):
                    if not prev or prev[-1] <= nums[i]:
                        if len(prev):
                            res.add(tuple(prev + [nums[i]]))
                        dfs(nums[i+1:], prev + [nums[i]])
        res = set()
        dfs(nums, [])
        return res
        