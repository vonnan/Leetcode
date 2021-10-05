class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n ==1:
            return False
        
        for i in range(1, n):
            if n % i== 0:
                if s[:i] * (n//i) == s:
                    return True
                
        return False