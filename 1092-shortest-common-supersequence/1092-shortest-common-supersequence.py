class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[""]* (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                if str1[r] == str2[c]:
                    dp[r+1][c+1] = dp[r][c] + str1[r]
                else:
                    dp[r+1][c+1] = max(dp[r+1][c], dp[r][c+1], key = len)
        print(dp[-1][-1])
        res, r,c, LCS = "", 0, 0, dp[-1][-1]
        for ch in LCS:
            while r < m and str1[r] != ch:
                res += str1[r]
                r += 1
            while c < n and str2[c] != ch:
                res += str2[c]
                c += 1
            res += ch
            r += 1
            c += 1
        return res + str1[r:] + str2[c:]
            
        
        
        
        
        
            
        