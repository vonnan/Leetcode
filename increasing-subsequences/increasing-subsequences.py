class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, pre):
            if nums:
                for i in range(len(nums)):
                    if not pre or nums[i] >= pre[-1]:
                        if len(pre):
                            result.add(tuple(pre + [nums[i]]))
                        dfs(nums[i+1:], pre + [nums[i]])
        
        result = set()
        dfs(nums, [])
        return result