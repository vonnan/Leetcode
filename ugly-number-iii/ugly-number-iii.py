from math import gcd
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a,b):
            return a*b//gcd(a,b)
        
        def count_ugly(m, a,b,c,ab, bc, ca,abc):
            ct = m//a + m//b + m//c
            ct -= m//ab + m//bc + m//ca
            ct += m//abc
            return ct
        
        ab, bc, ca = lcm(a, b), lcm(b, c), lcm(c, a)
        abc = lcm(ab, c)
        lo, hi = 1, 2* 10**9
        while lo < hi:
            mid = (lo + hi)//2
            if count_ugly(mid, a, b, c, ab, bc, ca, abc) < n:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
        
            
        