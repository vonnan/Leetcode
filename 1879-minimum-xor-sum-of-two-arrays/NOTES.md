```
class Solution:
def minimumXORSum(self, A, B):
n = len(A)
​
@lru_cache(None)
def dp(mask, i):
if i == n: return 0
return min(dp(mask ^ (1<<j), i + 1) + (A[i]^B[j]) for j in range(n) if mask & 1<<j)
​
return dp((1<<n) - 1, 0)
```