class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if arr == sorted(arr):
            return 0
        n = len(arr)
        front, back = [arr[0]], [arr[-1]]
        for a in arr[1:]:
            if a < front[-1]:
                break
            else:
                front.append(a)
        
        for b in arr[:-1][::-1]:
            if b > back[-1]:
                break
            else:
                back.append(b)
                
        back = back[::-1]
        nf, nb = len(front), len(back)
    
        res = n - max(nf, nb)
        while front:
            
            idx = bisect_left(back, front[-1])
            res = min(res, n - nf -(nb - idx))
            front.pop()
            nf -= 1
        
        return res
        
        
        
            
        
        