class Solution:
    def combinationSum(self, A: List[int], target: int) -> List[List[int]]:
        A.sort()
        
        res = set([])
        
        def dfs(pos, path, t):
            if t ==0:
                res.add(tuple(path))
                
            for i, a in enumerate(A[pos:], pos):
                if a > t:
                    break
                dfs(i, path + [a], t - a)
        
        dfs(0, [], target)
        return res