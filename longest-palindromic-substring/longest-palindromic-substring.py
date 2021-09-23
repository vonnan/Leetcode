class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = 1
        ans = s[0]
        for i in range(n):
            for j in range(n, i, -1):
                t = s[i:j]
                if t== t[::-1]:
                    if j - i > res:
                        ans = t
                        res = j - i
                    break
                        
        return ans