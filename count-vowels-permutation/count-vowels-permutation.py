class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, o, i, e, u = 1, 1, 1, 1, 1
        n-= 1
        while n:
            n -= 1
            a, o, i, e, u = e, i + u, a + o + e + u, a + i, a
        return (a+o+i+e+u) % (10**9+7)