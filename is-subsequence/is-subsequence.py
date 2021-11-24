class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        while s and t:
            if s[-1] == t[-1]:
                s.pop()
                t.pop()
            else:
                t.pop()
        return True if not s else False