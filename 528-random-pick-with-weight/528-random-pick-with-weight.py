from bisect import bisect_left
from random import randint

class Solution:

    def __init__(self, w: List[int]):
        self.w = list(accumulate(w))

    def pickIndex(self) -> int:
        num = randint(1, self.w[-1])
        idx = bisect_left(self.w, num)
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()