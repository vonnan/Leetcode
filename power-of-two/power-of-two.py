class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        sets = set([2 ** i for i in range(31)])
        
        return n in sets