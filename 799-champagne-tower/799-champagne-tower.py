
class Solution:
    def champagneTower(self, poured: int, row: int, glass: int) -> float:
        dp = [[0] * (r+1) for r in range(101)]
        dp[0][0] = poured
        
        for r in range(1, row + 1):
            for c in range(r):
                q = (dp[r-1][c] - 1.0)/2
                if q >0:
                    dp[r][c] += q
                    dp[r][c+1] += q
        
        return min(dp[row][glass],1)
            