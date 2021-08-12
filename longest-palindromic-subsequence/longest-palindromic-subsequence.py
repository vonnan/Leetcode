class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)
        
        memo = {}
        
        def dp(i, j):
            if (i, j) not in memo:
                if i > j:
                    memo[(i,j)] = 0
                elif i == j:
                    memo[(i,j)] = 1
                else:
                    if s[i] == s[j]:
                        memo[(i, j)] = 2+ dp(i+1, j-1)
                    else:
                        memo[(i, j)] = max(dp(i+1, j), dp(i, j-1))
            return memo[(i, j)]
        
        return dp(0, len(s) - 1)
                