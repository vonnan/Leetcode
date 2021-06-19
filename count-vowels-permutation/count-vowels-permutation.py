class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        mod = 10 ** 9 + 7
        n -= 1
        while n:
            a, e, i, o, u = e, a + i, a + e + o + u, i + u, a
            n -= 1
        return (a + e + i + o + u) % mod