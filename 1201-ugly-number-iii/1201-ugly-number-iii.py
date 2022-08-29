from math import gcd
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a, b):
            return a * b // (gcd(a, b))
        
        def ct_ugly(m):
            ct = m // a + m//b + m//c
            ab, bc, ca = lcm(a, b), lcm(b, c), lcm(c, a)
            abc = lcm(ab, c)
            ct -= m//ab + m// bc + m//ca
            ct += m//abc
            return ct
        
        left, right = 1, 2 * 10 **9 + 1
        while left < right:
            mid = (left + right)//2
            if ct_ugly(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left