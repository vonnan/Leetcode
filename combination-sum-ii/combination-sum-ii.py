from bisect import bisect
class Solution:
    def combinationSum2(self, A: List[int], target: int) -> List[List[int]]:
        A.sort()
        res = []
        
        def dfs(curr, pos, target):
            if target == 0:
                res.append(curr.copy())
            
            if target <= 0:
                return
            prev = -1
            for i in range(pos, len(A)):
                a = A[i]
                if a == prev:
                    continue
                curr.append(a)
                dfs(curr, i +1, target - a)
                curr.pop()
                prev = a
        
        dfs([], 0, target)
        
        return res
        
        
        