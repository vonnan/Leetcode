class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def LongestPal(s):
            if s == s[::-1]:
                return len(s)
            
            memo = {}
            def dp(i,j):
                if i > j:
                    return 0
                
                if i == j:
                    return 1
                
                if (i,j) in memo:
                    return memo[i, j]
                
                if s[i] == s[j]:
                    memo[i, j] = 2 + dp(i+1, j-1)
                else:
                    memo[i, j] = max(dp(i+1, j), dp(i, j -1))
                
                return memo[i, j]
            return dp(0, len(s)-1)
            
        return len(s) - LongestPal(s) <= k