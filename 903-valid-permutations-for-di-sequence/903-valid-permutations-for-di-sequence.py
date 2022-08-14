class Solution:
    def numPermsDISequence(self, S):
        dp = [1] * (len(S) + 1)
        for a, b in zip('I' + S, S):
            dp = list(itertools.accumulate(dp[:-1] if a == b else dp[-1:0:-1]))
        return dp[0] % (10**9 + 7)
    
    