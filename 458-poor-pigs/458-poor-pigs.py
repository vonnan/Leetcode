from math import ceil
class Solution:
    def poorPigs(self, buckets: int, Die: int, Test: int) -> int:
        if buckets == 1:
            return 0
        
        m = Test// Die
        
        pigs = 0
        while (m + 1)** pigs < buckets:
            pigs += 1
        return pigs