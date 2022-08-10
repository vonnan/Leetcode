class Solution:
    def combinationSum(self, A: List[int], target: int) -> List[List[int]]:
        A.sort()
        res = []
        
        def dfs(pos, path, t):
            if t == 0:
                res.append(tuple(path))
            
            for i, num in enumerate(A[pos:], pos):
                if num <= t:
                    dfs(i, path + [num], t- num)
            
        dfs(0, [], target)
        return res
                