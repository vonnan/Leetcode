class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        
        dp= [[[0, 0, 0, 0]] *(col+ 1) for _ in range(row)]
        
        res = 0
        for r in range(row):
            for c in range(col):
                if mat[r][c]:
                    dp[r][c] = [1] * 4
                    if r == 0 and c == 0:
                        res = max(res, 1)
                    
                    elif r == 0:
                        dp[r][c][0] += dp[r][c-1][0]
                    
                    elif c == 0:
                        dp[r][c][1] += dp[r-1][c][1]
                        dp[r][c][2] += dp[r-1][c+1][2]
                        
                        
                    else:
                        dp[r][c][0] += dp[r][c-1][0]
                        dp[r][c][1] += dp[r-1][c][1]
                        dp[r][c][2] += dp[r-1][c+1][2]
                        dp[r][c][3] += dp[r-1][c-1][3]
                    res = max(res, max(dp[r][c]))
        
        return res
                        
                        
                        
                        
