class Solution:
    def countDistinct(self, s: str) -> int:
        n = len(s)
        res = set([])
        for i in range(n):
            for j in range(i + 1, n + 1):
                res.add(s[i:j])
        return len(res)