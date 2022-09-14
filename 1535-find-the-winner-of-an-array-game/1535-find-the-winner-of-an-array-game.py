class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        ct = 0
        if k >= len(arr) -1:
            return max(arr)
        
        ct = 0
        
        while arr:
            if len(arr) == 1:
                return arr[0]
            
            if arr[0] > arr[1]:
                arr.pop(1)
                ct += 1
                
            else:
                arr.pop(0)
                ct = 1
            
            if ct == k:
                return arr[0]
            
            
            
            