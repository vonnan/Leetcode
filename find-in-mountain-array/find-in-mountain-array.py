# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        left, right = 0, n-1
        if mountain_arr.get(left) == target:
            return left
        
        while left < right:
            mid = (left + right)//2
            m = mountain_arr.get(mid)
            nxt = mountain_arr.get(mid+1)
            if  m < nxt:
                left = mid + 1
            else:
                right = mid
        
        peak = left
        print(peak)
        left, right = 0, peak
        
        while left < right:
            mid = (left + right)//2
            m = mountain_arr.get(mid)
            if m == target:
                return mid
            elif m<target:
                left = mid + 1
            else:
                right = mid
                
        if mountain_arr.get(left) == target:
            return left
        
        
        left, right = peak, n-1
        
        while left < right:
            mid = (left + right)//2
            m = mountain_arr.get(mid)
            if m == target:
                return mid
            elif m> target:
                left = mid + 1
            else:
                right = mid
          
        if mountain_arr.get(left) == target:
            return left
        return -1
                
                
                
                    