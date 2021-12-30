class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        
        def dp(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
                
            if (i, j) not in memo:
                if s[i] == s[j]:
                    memo[(i, j)] = dp(i + 1, j - 1) + 2
                else:
                    memo[(i, j)] = max(dp(i, j - 1), dp(i + 1, j))
            
            return memo[(i, j)]
        
        return dp(0, len(s) - 1)