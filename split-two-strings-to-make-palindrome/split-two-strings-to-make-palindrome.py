class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
    
        rev_a, rev_b = a[::-1], b[::-1]
        if b== rev_b or a== rev_a:
            return True
        
        i = 1
        while rev_b[:i] == a[:i]:
            i += 1
            
        
        j = 1
        while rev_a[:j] ==b[:j]:
            j += 1
            
        i-=1
        j-= 1
        
        return a[:i] + b[i:] == (a[:i] + b[i:])[::-1] or b[:j] + a[j:] == (b[:j] + a[j:])[::-1] or a[:n-i] + b[n-i:] == (a[:n-i] + b[n-i:])[::-1] or ( b[:n-j] + a[n-j:] == (b[:n-j] + a[n-j:])[::-1])
            
       