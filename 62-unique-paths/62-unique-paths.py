class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(x):
            if x == 0:
                return 1
            return x * factorial( x- 1)
        
        return factorial(m + n - 2)//factorial(m -1)// factorial(n - 1)
