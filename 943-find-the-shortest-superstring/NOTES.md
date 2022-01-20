```
class Solution:
def shortestSuperstring(self, A):
@lru_cache(None)
def suff(w1, w2):
return [w2[i:] for i in range(len(w1) + 1) if w1[-i:] == w2[:i] or not i][-1]
@lru_cache(None)
def dp(mask, l):
if mask + 1 == 1<<N: return ""
return min([suff(A[l], A[i]) + dp(mask | 1<<i, i) for i in range(N) if not mask & 1<<i], key = len)
N = len(A)
return min([A[i] + dp(1<<i, i) for i in range(N)], key=len)
```