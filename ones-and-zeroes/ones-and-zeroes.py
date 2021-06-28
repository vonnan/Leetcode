class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strs= [(s.count("0"), s.count("1")) for s in strs]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for zero, one in strs:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i + zero <= m and j + one <= n:
                        dp[i+zero][j + one] = max(dp[i+zero][j + one], dp[i][j] + 1)
        
        return dp[-1][-1]
            
            
            
            