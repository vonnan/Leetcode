class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
        res = []
        def dfs(s):
            if s.isdigit():
                return [int(s)]
            
            for i,c in enumerate(s):
                if c in ops:
                    left = self.diffWaysToCompute(s[:i])
                    right = self.diffWaysToCompute(s[i+1:])
                    res.extend([ops[c](l, r) for l in left for r in right])
            return res
        
        return dfs(expression)
            