class Solution:
    def makesquare(self, A: List[int]) -> bool:
        tot, n = sum(A), len(A)
        if n < 4 or tot % 4:
            return False
        A.sort(reverse = 1)
        
        target = tot//4
        
        if A[0] > target:
            return False
        
        @lru_cache(None)
        def dfs(mask, side, t):
            if mask == 0 and side == 0:
                return True
            
            for i in range(n):
                if mask & (1 << i):
                    if A[i] > t:
                        break
                    
                    mask_nxt = mask ^ ( 1<<i)
                    if A[i] == t:
                        if dfs(mask_nxt, side -1, target):
                            return True
                    else:
                        if dfs(mask_nxt, side, t - A[i]):
                            return True
            return False
        
        return dfs((1<<n)-1, 4, target)