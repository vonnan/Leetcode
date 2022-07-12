# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        left, right = 0, n -1
        while left < right:
            mid = (left + right)//2
            if n %2:
                val = reader.compareSub(left, mid-1, mid + 1, right)
                if n == 1 or  val== 0:
                    return mid
                elif val > 0:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                val = reader.compareSub(left, mid, mid + 1, right)
                if val > 0:
                    right = mid
                else:
                    left = mid + 1
            n = right - left + 1
            
        return left
        
    
                