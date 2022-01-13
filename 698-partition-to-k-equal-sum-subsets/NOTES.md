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