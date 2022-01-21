from itertools import combinations

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        dp = [n] * (1<<n)
        dp[0] = 0
        prereq = [0] * n
        
        for u, v in relations:
            prereq[v-1] |= 1 <<(u-1)
            
        for mask in range(1 << n):
            available = []
            for u in range(n):
                if mask & ( 1<< u) == 0 and (prereq[u] & mask == prereq[u]):
                    available.append(u)
            
            m = len(available)
            for choice in combinations(available, min(k, m)):
                mask2 = mask
                for v in choice:
                    mask2 |= (1 <<v)
                dp[mask2] = min(dp[mask2], 1 + dp[mask])
            
        return dp[-1]