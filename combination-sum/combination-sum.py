class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set([])
        nums.sort()
        n = len(nums)
        
        def dfs(remaining, pos, path):

            if remaining == 0:
                res.add(tuple(path))
            else:    
                for i in range(pos, n):
                    if nums[i] > remaining:
                        break
                    dfs(remaining - nums[i], i, path + [nums[i]])
                
        dfs(target, 0, [])
        
        return res
    
                
        