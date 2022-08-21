class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        n = len(s)
        if k == 1:
            return min(s[i:] + s[:i] for i in range(n))
        return "".join(sorted(list(s)))