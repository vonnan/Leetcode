# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, A: 'BinaryMatrix') -> int:
        row, col = A.dimensions()
        
        res = col - 1
        flag = False
        for r in range(row):
            if not A.get(r, res):
                continue
            left, right = 0, res
            while left < right:
                mid = (left + right)//2
                if A.get(r, mid):
                    right = mid
                else:
                    left = mid + 1
            
            if A.get(r, left):
                flag = True
                res = left
                
        return res if flag else -1