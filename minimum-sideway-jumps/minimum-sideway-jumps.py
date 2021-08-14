class Solution:
    def minSideJumps(self, A: List[int]) -> int:
        dp = [1, 0, 1]
        
        for a in A:
            if a!= 0:
                dp[a - 1] = inf
            for i in range(3):
                if i != a-1:
                    dp[i] = min(dp[i], dp[(i+1)%3] + 1, dp[(i+2)%3] + 1)
        
        return min(dp)