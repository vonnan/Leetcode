class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        dic = {}
        if len(s) != len(pattern):
            return False
        seen = set([])
        for i, c in enumerate(pattern):
            if c in dic:
                if dic[c] != s[i]:
                    return False
            else:
                if s[i] in seen:
                    return False
                dic[c] = s[i]
                seen.add(s[i])
        return True
                