from bisect import bisect_left

class Solution:
    def minWindow(self,S: str, T: str) -> str:
        row, col = len(T), len(S)
        dp = [[inf]* (col + 1) for _ in range(row+1)]
        
        for r in range(row):
            for c in range(col):
                if S[c] == T[r]:
                    if r== 0:
                        dp[r+1][c+1] = 1
                    else:
                        dp[r+1][c+1] = 1 + dp[r][c]
                else:
                    dp[r+1][c+1] = 1 + dp[r + 1][c]
        #print(dp)
        min_ = min(dp[-1])
        if min_ == inf:
            return ""
        
        dp2 = dp[-1]
        for c in range(min_, col+1):
            if dp2[c] == min_:
                return S[c - min_: c]
        
        
        
        
        
            
        
        
        
