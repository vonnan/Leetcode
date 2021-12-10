class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n ==3:
            return 2
        res = n//2 * (n - n//2)
        m = n//3
        
        if n % 3 == 0:
            res = max(res, 3 ** m)
        elif n% 3== 1:
            res = max(res, 3 ** (m-1) * 4)
        else:
            res = max(res, 3 ** m * 2)
        
        return res
        