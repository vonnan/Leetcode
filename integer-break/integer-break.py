class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        m = n//3
        
        if n % 3 == 1:
            return pow(3, m-1) * 4
        
        elif n % 3 == 0:
            return pow(3, m)
        
        else:
            return pow(3, m) * 2