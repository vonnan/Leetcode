class Solution:
    def combinationSum2(self, A: List[int], target: int) -> List[List[int]]:
        n, res = len(A), set()
        A.sort()
       
        def dfs(pos, path, target):
            if target == 0:
                res.add(tuple(path))
            
            if target < 0:
                return
            
            for i, num in enumerate(A[pos:], pos):
                if num > target:
                    break
                if i > pos and A[i-1] == num:
                    continue
                dfs(i + 1, path + [num], target - num)
                
        dfs(0, [], target)
        return res