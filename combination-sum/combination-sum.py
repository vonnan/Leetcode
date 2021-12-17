class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n, res = len(candidates), set([])
        
        def dfs(remaining, pos, path):
            if remaining == 0:
                res.add(tuple(path))
                
            else:
                for i, num in enumerate(candidates[pos:], pos):
                    if num <= remaining:
                        dfs(remaining - num, i, path + [num])
                    else:
                        break
        dfs(target, 0, [])
        return res