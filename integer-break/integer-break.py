class Solution:
    def integerBreak(self, n: int) -> int:
        
        res = (n//2) * (n - n//2)
        if n <=3:
            return res
        q, r = divmod(n, 3)
        
        if r ==0:
            return max(res, 3 ** q)
        
        elif r == 1:
            return max(res, 3 **(q-1) * 4)
        
        elif r== 2:
            return max(res, 3 ** q * 2)