class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set([])
        def dfs(output, left, right):
            if len(output) == 2*n:
                res.add(output)
            if left < n:
                dfs(output + "(", left + 1, right)
            if right < n and right < left:
                dfs(output + ")", left, right +1)
        dfs("(", 1, 0)
        return res