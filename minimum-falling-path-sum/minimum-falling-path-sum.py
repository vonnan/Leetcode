class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        if col == 1:
            return sum(sum(rows) for rows in matrix)
        dp = [0]*col
        for rows in matrix:
            dp2 =[0] * col
            for c in range(col):
                dp2[c] = rows[c]
                if c ==0:
                    dp2[c] +=  min(dp[c], dp[c+1])
                elif c== col-1:
                    dp2[c] += min(dp[c-1], dp[c])
                else:
                    dp2[c] += min(dp[c-1], dp[c], dp[c+1])
            dp = dp2[:]
            
        return min(dp)
                
            