class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        status = [False] * (n+1)
        path =[0]* n
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