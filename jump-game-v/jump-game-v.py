from collections import defaultdict

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n= len(arr)
        dp = [1]* n
        
        lst = sorted([(a,i) for i, a in enumerate(arr)])
        
        for a, i in lst:
            
            for j in range(i+1, min(i+d+1, n)):
                if arr[j] >= a:
                    break
                else:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
            for k in range(i-1, max(-1, i - d -1), -1):
                if arr[k] >= a:
                    break
                else:
                    dp[i] = max(dp[i], dp[k] + 1)
                   
        return max(dp)
       
    
        
                    
        
                    
        