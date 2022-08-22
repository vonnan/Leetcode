class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        sets = set([pow(4, i) for i in range(17)])
        return n in sets