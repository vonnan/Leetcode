class Solution:
    def palindromePartition(self, c: str, k: int) -> int:
        if len(c) == k:
            return 0
        memo = defaultdict(int)
        
        def dp(s,e,k):
            if (s,e,k) not in memo:
                if e - s + 1 < k:
                    memo[(s,e,k)] = inf
                elif k == 1:
                    memo[(s,e,k)] = sum((c[s + i] != c[e - i]) for i in range((e-s)//2 + 1))
                else:
                    
                    memo[(s,e,k)] = min(dp(s, i, k-1) + dp(i+1, e, 1) for i in range(s,e))
            return memo[(s,e,k)]
        
        return dp(0, len(c)-1, k)
                
            
            
        