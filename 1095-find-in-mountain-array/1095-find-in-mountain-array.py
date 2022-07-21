# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, A: 'MountainArray') -> int:
        n = A.length()
        left, right = 0, n - 1
        if A.get(left) == target:
            return left
        
        if target < A.get(left) and target < A.get(right):
            return -1
        
        #find pivot
        
        while left < right:
            mid = (left + right)//2
            num = A.get(mid)
            nxt = A.get(mid + 1)
            if num < nxt:
                left = mid + 1
            else:
                right = mid
        
        pivot = left
                    
        if target > A.get(pivot):
            return -1
        elif target == A.get(pivot):
            return pivot
        
        #check left
        
        left, right = 0, pivot
        
        while left < right:
            mid = (left + right)//2
            num = A.get(mid)
            #print(mid, num)
            if num == target:
                return mid
            elif num < target:
                left = mid + 1
            else:
                right = mid
        
        if A.get(left) == target:
            return left
        
        left, right = pivot, n-1
        #print(pivot)
        while left < right:
            mid = (left + right)//2
            
            num = A.get(mid)
            print(mid, num)
            if num == target:
                return mid
            elif num > target:
                left = mid + 1
            else:
                right = mid
        
        if A.get(left) == target:
            return left
        
        return -1
        
        
        
        
                