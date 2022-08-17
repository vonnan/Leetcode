class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def check(l,r):
            while l >=0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return s[l:r + 1]
        
        res = s[0]
        for i, c in enumerate(s):
            ans = check(i, i)
            if len(ans) > len(res):
                res = ans
            if i < n - 1 and s[i] == s[i+1]:
                ans = check(i, i + 1)
                if len(ans) > len(res):
                    res = ans
        return res
                
            