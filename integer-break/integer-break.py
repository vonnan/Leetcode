class Solution:
    def integerBreak(self, n: int) -> int:
        max_p = (n-n//2)*(n//2)
        if n <=4:
            return max_p
        for i in range(2, int(n//2)+1):
            m = n//i
            k = n % i
            product = m**(i-k)*(m+1)**k
            if product > max_p:
                max_p = product
        return max_p
            
            