class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count =0
        def isPalindrom(s):
            return s == s[::-1]
        for i in range(n):
            for j in range(i+1, n+1):
                if isPalindrom(s[i:j]):
                    count += 1
        return count
                