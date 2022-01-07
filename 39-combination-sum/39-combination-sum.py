class Solution:
    def combinationSum(self, A: List[int], target: int) -> List[List[int]]:
        A.sort()
        n, res = len(A), set()
        
        def dfs(remaining, pos, path):
            if remaining == 0:
                res.add(tuple(path))
            else:
                for i in range(pos, n):
                    if A[i] > remaining:
                        break
                    dfs(remaining - A[i], i, path + [A[i]])
        
        dfs(target, 0, [])
        return res