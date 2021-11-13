class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = 1
        ans = s[0]
        for i in range(n):
            for j in range(n , i + res, -1):
                if s[i: j] == s[i:j][::-1]:
                    if j - i > res:
                        ans = s[i:j]
                        res = j - i
        
        return ans