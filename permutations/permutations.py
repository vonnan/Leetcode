class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0 for _ in range(n)]
        status = [False for _ in range(n+1)]
        res = set()
        
        def dfs(u):
            if u == n:
                res.add(tuple(path[:]))
                return 
    
            for j in range(n):
                if not status[j]:
                    status[j] = True
                    path[u] = nums[j]
                    dfs(u+1)
                    status[j] = False
        
        dfs(0)
        
        return res