class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x = int(dividend/divisor)
        return x if-2**31 <= x < 2**31 else 2 **31 -1