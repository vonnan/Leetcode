class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n, res = len(candidates), set([])
        candidates.sort()
        
        def dfs(remaining, pos, path):
            if remaining == 0:
                res.add(tuple(path))
                
            else:
                for i in range(pos, n):
                    if candidates[i] > remaining:
                        break
                    dfs(remaining - candidates[i], i, path + [candidates[i]])
        
        dfs(target, 0, [])
        return res
            
            