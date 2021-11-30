class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        n = len(A)
        if n < d:
            return -1
        @lru_cache(None)
        def dp(pos, day):
            if day == 1:
                return max(A[pos:])
            
            max_, res = 0, inf
            for j in range(pos, n + 1 - day):
                max_ = max(max_, A[j])
                res = min(res, max_ + dp(j+1, day - 1))
            return res
                
        return dp(0, d)