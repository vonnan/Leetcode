class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}
        n = len(values)
        
        for i in range(n-1):
            memo[i, i+1] = 0
            
        for delta in range(2, n):
            for i in range(n - delta):
                j = i + delta
                memo[i, j] = min(memo[i, k] + memo[k, j ] + values[i] * values[j] * values[k] for k in range(i+1, j))
        
        return memo[0, n-1]