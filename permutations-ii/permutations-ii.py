class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        nums.sort()
        
        
        def dfs(nums, ans):
            if len(ans) ==n:
                res.append(ans)
                return
            for i in range(len(nums)):
                if i > 0 and (nums[i] == nums[i-1]):
                    continue
                dfs(nums[:i] + nums[i+1:], ans + [nums[i]])
                    
        dfs(nums, [])
        return res