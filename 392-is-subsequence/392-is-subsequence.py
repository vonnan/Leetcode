class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not t:
            if not s:
                return True
            else:
                return False
        s, t = list(s), list(t)
        while s and t:
            x = s.pop()
            while t and t[-1] != x:
                t.pop()
            if not t:
                return False
            t.pop()
        return True
                