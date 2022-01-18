```
def dfs(bitmask):
if bitmask == 0: return 0
cand = 0
n_z_bits = [j for j in range(n) if bitmask&(1<<j)]
for j, k in combinations(n_z_bits, 2):
q = bitmask^(1<<j)^(1<<k)
cand = max(cand, dfs(q) + (n+2 - len(n_z_bits))//2*gcds[j, k])
return cand
​
return dfs((1<<n) - 1)
​
```