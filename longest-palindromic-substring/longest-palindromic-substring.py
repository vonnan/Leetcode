class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, n = "", len(s)
        
        def helper(s,l,r):
            while l >=0 and r < n and s[l] ==s[r]:
                l -= 1
                r += 1
            return s[l+ 1:r]
        
        for i in range(n):
            res = max(res, helper(s,i,i), helper(s, i, i + 1), key = len)
        return res