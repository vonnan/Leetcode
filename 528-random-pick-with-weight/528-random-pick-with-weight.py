from random import randint
from bisect import bisect_left

class Solution:

    def __init__(self, w: List[int]):
        self.lst = list(accumulate(w))
        

    def pickIndex(self) -> int:
        num = randint(1, self.lst[-1])
        return bisect_left(self.lst, num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()