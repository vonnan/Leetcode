class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set([])
        
        def dfs(path, left, right):
            if len(path) == 2* n:
                res.add(path)
                return
                
            if left < n:
                dfs(path + "(", left + 1, right)
            if right < n and left > right:
                dfs(path + ")", left, right + 1)
                
        dfs("", 0, 0)
        
        return res
                
                