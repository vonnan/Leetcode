class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, n = set(), len(nums)
        nums.sort()
        
        visited = [0] * n
        def dfs(nums, ans, n):
            if len(ans) ==n:
                res.add(tuple(ans[:]))
                return
            for i in range(len(nums)):
                if i > 0 and (nums[i] == nums[i-1]):
                    continue
                dfs(nums[:i] + nums[i+1:], ans + [nums[i]], n)
                    
        dfs(nums, [], n)
        return res