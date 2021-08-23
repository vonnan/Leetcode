class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        if b == 0:
            return a
        if b & mask == 0:
            return a & mask
        return self.getSum(a ^ b, (a & b)<< 1)