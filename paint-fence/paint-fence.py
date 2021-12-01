class Solution:
    def numWays(self, n: int, k: int) -> int:
        prev, curr = k, k ** 2
        for _ in range(n-1):
            prev, curr = curr, (k-1)*(prev + curr)
        return prev
    