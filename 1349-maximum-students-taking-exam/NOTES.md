```
class Solution:
def maxStudents(self, seats):
m, n = len(seats), len(seats[0])
masks = []
​
for row in seats:
mask = sum((1 << j)*(v==".") for j, v in enumerate(row))
masks.append([i for i in range(1<<n) if i & mask == i and not i & (i>>1)])
@lru_cache(None)
def dp(curr, i):
if i == -1: return 0
res = 0
for prev in masks[i-1]:
if not (curr >> 1) & prev and not curr & (prev >> 1):
res = max(res, dp(prev, i - 1))
​
return res + bin(curr).count("1")
​
return max(dfs(mask, m-1) for mask in masks[m-1])
```