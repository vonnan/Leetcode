from random import randint
from bisect import bisect_left
class Solution:

    def __init__(self, w: List[int]):
        self.lst = w
        for i in range(1, len(w)):
            self.lst[i] += self.lst[i-1]
            
    def pickIndex(self) -> int:
        val = randint(1, self.lst[-1])
        return bisect_left(self.lst, val)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()