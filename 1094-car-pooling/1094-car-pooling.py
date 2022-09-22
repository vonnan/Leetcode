class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dp = [0] * 1001
        max_ = 0
        for num, a, b in trips:
            dp[a] += num
            dp[b] -= num
            max_ = max(max_, b)
        
        if dp[0] > capacity:
            return False
        
        for i in range(1, max_):
            dp[i] += dp[i-1]
            if dp[i] > capacity:
                return False
        return True
            