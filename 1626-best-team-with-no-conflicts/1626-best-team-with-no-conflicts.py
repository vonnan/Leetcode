from bisect import insort
from bisect import bisect

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        lst = sorted([(age, score) for score, age in zip(scores, ages)])
        n = len(scores)
        dp = [0] * n
        res = 0
        
        scores = [score for _, score in lst]
        
        for i, score in enumerate(scores):
            dp[i] = score
            for j in range(i):
                if scores[j] <= score:
                    dp[i] = max(dp[i], dp[j] + score)
        
        return max(dp)
        
        
        
        
        