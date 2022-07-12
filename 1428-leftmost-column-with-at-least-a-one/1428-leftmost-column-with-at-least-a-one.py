# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self,B: 'BinaryMatrix') -> int:
        row, col = B.dimensions()
        res = inf
        for r in range(row):
            left, right = 0, col - 1
            if B.get(r, right) == 0:
                continue
            while left < right:
                mid = (left + right)//2
                if B.get(r, mid) == 0:
                    left = mid + 1
                else:
                    right = mid
            
            res = min(res, left)
        return res if res != inf else -1
            