class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        sets = set([pow(3, i) for i in range(25)])
        return n in sets