class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10**9 + 7
        if p ==1:
            return 1
       
        else:
            x = pow(2, (p-1))
            y = 2*(x-1)
            return ((2*x-1)*pow(y, x-1, mod))% mod