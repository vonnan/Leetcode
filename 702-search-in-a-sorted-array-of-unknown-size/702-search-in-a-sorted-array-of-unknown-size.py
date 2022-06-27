# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 10**4
        max_ = 2**31 -1
        while left < right:
            mid = (left + right)//2
            if reader.get(mid) == target:
                return mid
            
            if reader.get(mid) == max_:
                right = mid
            if reader.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        
        return -1