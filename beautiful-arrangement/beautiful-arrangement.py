class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(pos, mask):
            if pos == 0:
                return 1
            
            res = 0
            for i in range(n):
                if mask & ( 1<<i) and (not (i + 1) % pos or not pos % ( i + 1)):
                    res += dfs(pos -1, mask ^ ( 1 << i))
            
            return res
        
        return dfs(n, (1 <<n) - 1)
                