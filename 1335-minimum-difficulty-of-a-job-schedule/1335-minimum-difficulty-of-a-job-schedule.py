class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        n = len(A)
        
        @lru_cache(None)
        def dp(pos, day):
            if day == 1:
                return max(A[pos:])
            
            res, max_ = inf, 0
            
            for i in range(pos, n - day + 1):
                max_ = max(A[i], max_)
                res = min(res, max_ + dp(i + 1, day -1))
            
            return res if res != inf else -1
        
        return dp(0, d)
        
        
