class Solution:
    def twoEggDrop(self, n: int) -> int:
        y = x = int((2 * n)**0.5)
        if y * (y + 1) == 2 * n:
            return y
        
        def dp(a):
            m, b = n, a
            ct = 0
            while a > 1:
                m -= a
                a -= 1
                ct += 1
            return max(b, ct + m)
        
        return min(dp(y), dp(y + 1))
