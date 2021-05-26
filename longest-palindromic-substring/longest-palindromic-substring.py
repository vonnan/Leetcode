class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrom(s):
            return s== s[::-1]
        
        res, ans = 0, ""
        
        for i in range(len(s)):
            for j in range(len(s), i+ res, -1):
                if isPalindrom(s[i:j]):
                    if j-i > res:
                        res = j-i
                        ans = s[i:j]
                        break
        return ans
                    