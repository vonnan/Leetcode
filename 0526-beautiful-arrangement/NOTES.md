def helper(nums, tmp):
if not nums:
self.res += 1
else:
for i in range(len(nums)):
if nums[i] % (len(tmp) + 1) == 0 or (len(tmp) + 1) % nums[i] == 0:
helper(nums[:i] + nums[i + 1:], tmp + [nums[i]])
helper(nums, [])
return self.res
```
​
```
class Solution:
def countArrangement(self, n: int) -> int:
@lru_cache(None)
def dfs(pos, mask):
if pos == 0:
return 1
res = 0
for i in range(n):
if mask & ( 1<<i) and (not (i + 1) % pos or not pos % ( i + 1)):
res += dfs(pos -1, mask ^ ( 1 << i))
return res
return dfs(n, (1 <<n) - 1)
```
Remark: this is so-called dynamic programming on subsets problem, which has similar ideas with TSP (travelling salesman problem). Usually you can recoginze these problems if dimension of data is around 10-20. Here is the list of similar problems on leetcode I found so far:
​
Problem 465 Optimal Account Balancing
​
Problem 473 Matchsticks to Square
​
​
Problem 698 Partition to K Equal Sum Subsets
​
Problem 847 Shortest Path Visiting All Nodes]