class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        
        dp = [[0] * (i+1) for i in range(1, n+1)]
        
        dp[0] = 1- prob[0], prob[0]
        
        for pos in range(1, n):
            p = prob[pos]
            if p == 0:
                dp[pos][:-1] = dp[pos-1][:]
            elif p == 1:
                dp[pos][0] = 0
                dp[pos][1:] = dp[pos-1][:]
            else:
                dp[pos][0] = dp[pos-1][0] * (1- p)
                dp[pos][-1] = dp[pos-1][-1] * p
                for ct in range(1, pos+1):
                    dp[pos][ct] = dp[pos-1][ct - 1] * p + dp[pos-1][ct] *(1-p)
                
        
        return dp[-1][target] 
        