class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        if not s or s == rev:
            return s
        n = len(s)
        for j in range(n-1, 0, -1):
            if s[:j] == rev[n-j:]:
                return s[j:][::-1] + s