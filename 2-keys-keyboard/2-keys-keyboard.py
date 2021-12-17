class Solution:
    def minSteps(self, n: int) -> int:
        
        res = 0
        if n == 1:
            return res
        prev = 2
        while n > 1:
            upper = int(n ** 0.5) + 1
            if n % prev:
                prev += 1
                continue
            else:
                while n >1 and n % prev == 0:
                    n //= prev
                    res += prev
                prev += 1
        return res
                        
        
                    
      
