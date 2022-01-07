class Solution:
    def numSquares(self, n: int) -> int:
        lst = [i *i for i in range(1, int(n **0.5) + 1)]
        lst.sort(reverse = 1)
        dp =[0]+ [inf]* n
        
        for i in range(1, n + 1):
            for coin in lst:
                if coin > i:
                    continue
                dp[i] = min(dp[i], dp[i- coin] + 1)
                
        return dp[-1]