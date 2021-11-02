class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = 1
        ans = ""
        
        for i in range(n- res + 1):
            for j in range(n, i + res-1, -1):
                t = s[i:j]
                if t == t[::-1]:
                    res = j - i
                    ans = t
                    break
        return ans