class Solution:
    @lru_cache(None)
    def numberOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        return sum(self.numberOfWays(i) * self.numberOfWays(n-2-i) for i in range(0, n, 2))% mod if n else 1