```
n = len(hats)
h2p = collections.defaultdict(list)
for p, hs in enumerate(hats):
for h in hs:
h2p[h].append(p)
full_mask = (1 << n) - 1
mod = 10**9 + 7
@functools.lru_cache(maxsize=None)
def count(h, mask):
# everyone wears a hat
if mask == full_mask:
return 1
# ran out of hats
if h == 41:
return 0
# skip the current hat h
ans = count(h + 1, mask)
for p in h2p[h]:
# if person p already has a hat
if mask & (1 << p):
continue
# let person p wear hat h
ans += count(h + 1, mask | (1 << p))
ans %= mod
return ans
# start from the first hat and no one wearing any hat
return count(1, 0)
```