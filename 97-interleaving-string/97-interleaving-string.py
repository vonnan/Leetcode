class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        
        @lru_cache(None)
        def dp(i, j, k):
            if i == l1 and j == l2 and k == l3:
                return True
            
            flag1, flag2 = False, False
            
            if i < l1 and  s1[i] == s3[k]:
                flag1 = dp(i+1, j, k + 1)
            
            if j < l2 and s2[j] == s3[k]:
                flag2 = dp(i, j + 1, k + 1)
                
            
            return flag1 or flag2
        
        return dp(0, 0, 0)
                
                