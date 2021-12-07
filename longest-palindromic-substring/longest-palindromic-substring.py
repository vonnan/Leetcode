class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, res = len(s), 1
        
        def helper(l,r):
            while l >=0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        
        res = s[0]
        
        for r in range(n):
            res = max(res, helper(r,r), helper(r, r+1), key = len)
            
        return res