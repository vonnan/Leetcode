class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        if m - p.count("*") > n:
            return False
        dp = [True] + [False] * n
        for c in range(m):
            if p[c] == "*":
                for r in range(n):
                    dp[r+1] = dp[r] | dp[r+1]
            else:
                for r in range(n-1, -1, -1):
                    dp[r+1] = dp[r] and (s[r] == p[c] or p[c] == "?")
                dp[0] = False
            
        return dp[-1]