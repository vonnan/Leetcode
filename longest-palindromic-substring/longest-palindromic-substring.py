class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, n = "", len(s)
        
        def p(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        
        for i, c in enumerate(s):
            res = max([res, p(i,i), p(i,i +1)], key = len)
        return res
            