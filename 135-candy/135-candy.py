class Solution:
    def candy(self, ratings: List[int]) -> int:
        ratings = [-inf] + ratings + [-inf]
        lst = sorted([(num, i) for i, num in enumerate(ratings)], reverse = 1)
        n = len(ratings)
        
        dp = [1] * n
        dp[0], dp[-1] = 0, 0
        
        lst.pop()
        lst.pop()
        
        while lst:
            _, i = lst.pop()
            if ratings[i-1] > ratings[i]:
                dp[i-1] = max(dp[i-1], dp[i] + 1)
            if ratings[i+1] > ratings[i]:
                dp[i+1] = max(dp[i+ 1], dp[i] + 1)
        
        if ratings[i] > ratings[i-1]:
            dp[i] = max(dp[i], dp[i-1] + 1)
        if ratings[i] > ratings[i+1]:
            dp[i] = max(dp[i], dp[i+ 1] + 1)
        
        return sum(dp[1:-1])
        
        
                
        
        