class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res =[]
        
        for d in range(2, 10):
            res.extend(int("".join([str(x) for x in range(i ,i + d)])) for i in range(1,11 - d))
        
        while res and res[0] < low:
            res.pop(0)
            
        while res and res[-1] > high:
            res.pop()
            
        return res
                
                