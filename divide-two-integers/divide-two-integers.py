class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = int(dividend/divisor)
        return ans if -2**31 <= ans <= 2**31-1 else 2**31-1