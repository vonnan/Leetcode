class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], A: List[int]) -> int:
        n = len(A)
        l, r = 0, n-1
        minl, minr = inf, inf
        
        lst = []
        
        while l <= r:
            minl = min(minl, A[l])
            minr = min(minr, A[r])
            if minl >= minr:
                lst.append(minl)
                l += 1
            else:
                lst.append(minr)
                r -= 1
                
        boxes.sort(reverse = 1)
        res = 0
        
        while boxes:
            while lst and lst[-1] < boxes[-1]:
                lst.pop()
          
            if not lst: 
                return res    
            lst.pop()
            boxes.pop()
            res += 1
            
            
        return res
        