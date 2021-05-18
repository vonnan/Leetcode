from random import randint
class Solution:

    def __init__(self, w: List[int]):
        self.w = list(accumulate(w))

    def pickIndex(self) -> int:
        r = randint(1, self.w[-1])
        left, right = 0, len(self.w)
        while left < right:
            mid = (left + right)//2
            if self.w[mid] == r:
                return mid
            elif self.w[mid] > r:
                right = mid
            else:
                left = mid + 1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()