
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        prefix = [0]
        n = len(stones)
        if (n - 1)% (k-1):
            return -1
        
        for stone in stones:
            prefix.append(prefix[-1] + stone)
            
        @lru_cache(None)
        def dp(i, j):
            if j - i + 1 < k:
                return 0
            
            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, k-1))
            if (j -i) % (k-1) == 0:
                res += prefix[j+ 1] - prefix[i]
                
            return res
        
        return dp(0, n-1)
        
            
            
                
    