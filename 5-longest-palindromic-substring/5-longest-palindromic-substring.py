class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def P(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        res = s[0]
        for i in range(n):
            res = max([res, P(i,i), P(i, i + 1)], key = len)
        
        return res
