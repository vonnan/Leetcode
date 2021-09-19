class Solution:
    def combinationSum2(self, A: List[int], target: int) -> List[List[int]]:
        n, res = len(A), set([])
        A.sort()
        curr = []
        def dfs(target, pos):
            if target == 0:
                res.add(tuple(curr))
            
            prev = -1
            for i, num in enumerate(A[pos:], pos):
                if num == prev:
                    continue
                if num > target:
                    break
                curr.append(num)
                dfs(target - num, i + 1)
                curr.pop()
                prev = num
        
        dfs(target, 0)
        
        return res
                
    