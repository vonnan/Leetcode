
class Solution:
    def pathsWithMaxScore(self, A: List[str]) -> List[int]:
        n, mod= len(A), 10 **9 + 7
        
        path = [(1,0), (0, 1), (1, 1)]
        
        dp = [[[-10**5,0]]* (n+1) for _ in range(n + 1)]
        dp[n-1][n-1] = [0, 1]
        print(dp)
        for r in range(n-1, -1,-1):
            for c in range(n-1, -1, -1):
                if A[r][c] in "XS":
                    continue
                for dr, dc in path:
                    nr, nc = r + dr, c + dc
                    #print(r, c, nr, nc, dr, dc, dp[r][c], dp[nr][nc])
                    if dp[r][c][0] < dp[nr][nc][0]:
                        dp[r][c] = [dp[nr][nc][0], 0]
                    if dp[r][c][0] == dp[nr][nc][0]:
                        dp[r][c][1] += dp[nr][nc][1]
                dp[r][c][0] += int(A[r][c]) if r or c else 0
        return [dp[0][0][0] if dp[0][0][1] else 0, dp[0][0][1] % mod]
                    
                
        