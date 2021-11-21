class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m -= 1
        n -= 1
        def factorial(x):
            if x == 0:
                return 1
            return x * factorial(x-1)
        
        return factorial(m + n)//(factorial(m) * factorial(n))