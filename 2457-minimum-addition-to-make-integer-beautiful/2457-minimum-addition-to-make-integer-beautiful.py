class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        i, orig = 0, n
        while sum(map(int, str(n))) > target:
            n = n//10 + 1
            i += 1
        return n * 10** (i) - orig