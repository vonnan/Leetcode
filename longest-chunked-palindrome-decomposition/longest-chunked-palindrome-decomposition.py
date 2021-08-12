class Solution:
    def longestDecomposition(self, text: str) -> int:
        res, n = 0, len(text)
        text = list(text)
        ans = []
        
        while text and n >=2:
            temp0, temp1 = text.pop(0), text.pop() 
            n -= 2
            
            while temp0 != temp1 and n >= 2:
                temp0 += text.pop(0)
                temp1 = text.pop() + temp1
                n -= 2
            if temp0 == temp1:
                res += 2
                ans.append(temp0)
            if n < 2: 
                return res + 1 if (n or temp0!= temp1) else res
            
        if n:
            ans.append("".join(text))
        
        
        return res + 1 if n else res
            
                
                
            