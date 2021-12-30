class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ct = 0
        
        def isP(x):
            return x == x[::-1]
        
        for i in range(n):
            for j in range(i+1):
                if isP(s[j:i+1]):
                    ct += 1
        return ct