
class Solution:
    def deleteString(self, s: str) -> int:
        if len(s) == len(set(s)):
            return 1
        
        if len(set(s)) ==1:
            return len(s)
        
        n = len(s)
        
        @lru_cache(None)
        def dp(i):
            res = 1
            
            for j in range(i + 1, n):
                if s[i] == s[j] and s[i:j] == s[j: j + (j - i)]:
                    res = max(res, 1 + dp(j))
            
            return res
        
        return dp(0)
                    
           
            