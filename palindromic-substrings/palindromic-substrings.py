class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        def isP(x):
            return x == x[::-1]
        ct = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if isP(s[i:j]):
                    ct += 1
        
        return ct