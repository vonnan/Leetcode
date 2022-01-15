from itertools import combinations

class Solution:
    def minNumberOfSemesters(self, n: int, A: List[List[int]], k: int) -> int:
        
        prereq = [0] * n
        for u,v in A:
            prereq[v-1] |= 1 << (u - 1)
            
        dp = [n] * (1 << n)
        dp[0] = 0
        
        for mask in range(1 << n):
            available = []
            
            for v in range(n):
                if mask & (1 <<v) == 0 and (mask & prereq[v] == prereq[v]):
                    available.append(v)
                    
            
            
            for choices in combinations(available, min(k, len(available))):
                mask2 = mask
                for v in choices:
                    mask2 |= 1<< v
            
                dp[mask2] = min(dp[mask2], 1+ dp[mask])
            
        return dp[-1]
                
                
        
        
            
        
            