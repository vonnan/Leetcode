```
class Solution:
def minNumberOfSemesters(self, n: int, dep, k: int) -> int:
​
reqs = [0]*n
for u,v in dep:
reqs[v-1]  |= 1<<(u-1)
dp = [n] * (1<<n)
dp[0] = 0
for mask in range(1<<n):
#in state of current mask,we should choose extra courses now.
#so,check for all the available courses.
avail = []
for v in range(n):
if mask & (1<<v) == 0 and  mask & reqs[v]  == reqs[v]:
avail.append(v)
# mask & (1<<v) tells which courses are not yet taken in state of mask
# mask & reqs[v] tells if reqs[v] is a subset of courses taken.
for choice in itertools.combinations(avail, min(k,len(avail)) ):
mask2 = mask #courses taken
for u in choice:
mask2 |= (1<<u)
#now,we have mask2 = (courses taken in mask + available courses)
#now do the PUSH-DP work
#since we are adding k new courses to the previous courses(mask),we might endup taking a new semester => dp[mask]+1
#but dp[mask2] might have been acheived in lesser semessters in another order i.e might have been reached mask2
#by another mask. In that case,we dont want to increase the no of semesters we need.
#so,we choose the minimum of either.
dp[mask2] = min(dp[mask2],1+dp[mask])
​
#finally return how many min semesters it takes to take all courses i.e dp[(1<<n)-1] which is of form 0b111111
return dp[-1]
```