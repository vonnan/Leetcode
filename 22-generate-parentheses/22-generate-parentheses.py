class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        
        def dfs(left, right, path):
            if len(path) == 2 * n:
                res.add(tuple(path))
                
            if left < n:
                dfs(left + 1, right, path + "(")
            
            if right < n and left > right:
                dfs(left, right + 1, path + ")")
                
        dfs(0,0, "")
        return ["".join(x) for x in res]