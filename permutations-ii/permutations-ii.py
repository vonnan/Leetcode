class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, n = set(), len(nums)
        nums.sort()
        visited = [0] * n
        def dfs(ans):
            if len(ans) ==n:
                res.add(tuple(ans[:]))
                return
            for i in range(n):
                
                if not visited[i]:
                    visited[i] = 1
                    dfs(ans+ [nums[i]] )
                    visited[i] = 0
                    
        dfs([])
        return res