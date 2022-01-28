```
class Solution:
def longestPalindromeSubseq(self, s: str) -> int:
memo = {}
def dp(l, r, prev):
if (l, r, prev) not in memo:
if l >= r:
return 0
if s[l] == s[r] and (s[l] != prev):
return 2 + dp(l + 1, r - 1, s[l])
memo[(l, r, prev)] = max(dp(l + 1, r, prev), dp(l, r - 1, prev))
return memo[(l, r, prev)]
return dp(0, len(s) - 1, '')
```
```
n = len(s)
# Define pairs to hold list of tuples (i, j) where s[i] == s[j] and pairs[k-1][0] < pairs[k][0],
# for all k in [1, len(pairs)-1]. That is, the pairs are sorted in increasing order by the left
# index value i.
pairs = []
# Define f[p] to hold the length of the longest good palindrome subsequence starting at p[0] and
# ending at p[1]
f = collections.defaultdict(int)
for i in range(len(s)):