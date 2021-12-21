class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        
        sets = set([2 ** i for i in range(32)])
        
        return n in sets