class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        
        @cache
        def partial(n):
            if n == 2:
                return 1
            return (partial(n-1) + full(n-2))%mod
        
        @cache
        def full(n):
            if n <= 2:
                return n
            
            return (full(n-1) + full(n-2) + 2 * partial(n-1))% mod
        
        return full(n) 