class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def fib(m):
            if m not in memo:
                if m <2:
                    memo[m] = m
                else:
                    memo[m] = fib(m-1) + fib(m-2)
                
            return memo[m]
        return fib(n)
            