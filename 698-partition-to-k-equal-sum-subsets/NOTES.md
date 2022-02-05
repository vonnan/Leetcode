```
n, tot = len(nums), sum(nums)
if tot %k:
return False
nums.sort(reverse = 1)
target = tot//k
@lru_cache(None)
def helper(mask, side, t):
if mask == 0 and side == 0:
return True
for i in range(n):
if mask & ( 1<< i):
if nums[i] > t:
break
mask_nxt = mask ^ (1 <<i)
if nums[i] == t:
if helper(mask_nxt, side -1, target):
return True
else:
if helper(mask_nxt, side, t - nums[i]):
return True
return False
return helper((1<<n)-1, k, target)
```
​
```
def canPartitionKSubsets(self, A, k):
if len(A) < k:
return False
ASum = sum(A)
A.sort(reverse=True)
if ASum % k != 0:
return False
target = [ASum / k] * k
​
def dfs(pos):
if pos == len(A): return True
for i in xrange(k):
if target[i] >= A[pos]:
target[i] -= A[pos]
if dfs(pos + 1):
return True
target[i] += A[pos]
return False
return dfs(0)
```