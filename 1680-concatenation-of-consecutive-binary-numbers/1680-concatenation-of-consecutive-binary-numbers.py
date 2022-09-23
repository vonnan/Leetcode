class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        mod = 10 ** 9 + 7
        
        for i in range(n):
            res += bin(i + 1)[2:]
        
        return int(res, 2) % mod
