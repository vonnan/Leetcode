class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        for c in s:
            if c.isalpha():
                res.append([c.upper(), c.lower()])
            else:
                res.append([c])
        return ["".join(x) for x in product(*res)]