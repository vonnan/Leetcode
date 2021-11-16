class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        
        for i in range(2, n +1):
            lst = [dp[j] * dp[i - 1 - j] for j in range(i)]
            
            dp[i] = sum(lst)
        
        return dp[-1]
        
        