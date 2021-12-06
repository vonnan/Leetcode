class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        if n ==1:
            return 1
        print(pairs)
        dp = [1] * n
        end = pairs[0][1]
        for i in range(1, n):
            s,e = pairs[i]
            if s > end:
                dp[i] = dp[i-1] + 1
                end = e
            else:
                dp[i] = dp[i-1]
                end = min(end, e)
        return dp[-1]
            