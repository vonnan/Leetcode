class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n ==2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        
        n1, n2 = n//2, n- n//2
        res = n1 * n2
        
        q,r = divmod(n, 3)
        if r == 1:
            return max(res, 3**(q-1) * 4)
        elif r == 0:
            return max(res, 3**q)
        else:
            return max(res, 3**q * 2)
        
            