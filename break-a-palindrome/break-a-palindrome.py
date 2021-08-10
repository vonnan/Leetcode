class Solution:
    def breakPalindrome(self, A: str) -> str:
        if len(A)==1:
            return ""
        if set(A) == set("a"):
            return A[:-1] + "b"
        
        res, i, n = "", 0, len(A)
        A= list(A)
        while A[0] == "a":
            res += "a"
            A.pop(0)
            i += 1
        
        if n %2 and i == n//2:
            return res + "".join(A[:-1]) + "b"
        
        else:
            return res + "a" + "".join(A[1:])
        
       
            
        
            
            