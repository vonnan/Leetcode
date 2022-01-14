class Solution:
    def countArrangement(self, n: int) -> int:
        
        @lru_cache(None)
        def dfs(mask, pos):
            if pos == 0:
                return 1
            
            res = 0
            
            for i in range(1, n+1):
                if (not mask &(1 <<i)) and (pos % i == 0 or (i % pos ==0)):
                    #print(bin(mask)[2:], i, res)
                    res += dfs(mask ^ ( 1 << i), pos - 1)
            
            return res
        
        return dfs(0, n)
 