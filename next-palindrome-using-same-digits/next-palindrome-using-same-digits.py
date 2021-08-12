class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        
        m = num[:n//2]
         
        def nextPal(s):
            i = j = len(s) -1
            s = [int(x) for x in s]
            print(s)
            while i > 0 and s[i-1] >= s[i]:
                i -= 1
                
            if i == 0:
                return ""
            
            else:
                while s[i-1] >= s[j]:
                    j -= 1
                
                s[i-1], s[j] = s[j], s[i-1]
                s[i:] = s[i:][::-1]
                s = [str(x) for x in s]
                return "".join(s)
              
        res = nextPal(m)
            
        return res + num[n//2: (n+1)//2] + res[::-1] if res else ""
                
                
            
        
        
            