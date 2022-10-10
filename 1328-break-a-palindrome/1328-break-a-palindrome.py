class Solution:
    def breakPalindrome(self, A: str) -> str:
        if len(A) == 1:
            return ""
        
        n = len(A)
        if set(A[:n//2]) == set(["a"]):
            return A[:-1] + "b"
        
        res = ""
        A = list(A)
        while A[0] == "a":
            res += A.pop(0)
        
        res += "a"
    
        return res + "".join(A[1:])
        
            
       
            
        
            
            