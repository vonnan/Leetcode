```
def maximumANDSum(self, A, ns):
@lru_cache(None)
def dp(i, mask):
res = 0
if i == len(A): return 0
for slot in range(1, ns + 1):
b = 3 ** (slot - 1)
if mask // b % 3 > 0:
res = max(res, (A[i] & slot) + dp(i + 1, mask - b))
return res
return dp(0, 3 ** ns - 1)
```