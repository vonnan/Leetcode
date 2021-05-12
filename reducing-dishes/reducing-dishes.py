class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        if satisfaction[-1]<= 0:
            return 0
    
        lst = [num * (i+1) for i, num in enumerate(satisfaction)]
        res = sum(lst)
        tot = sum(satisfaction)
        
        if tot >= 0:
            return res
        
        for i, num in enumerate(satisfaction):
            if num >= 0:
                 break
            
            if tot >= 0:
                return res
            
            else:
                res -= tot
                
            tot -= num
                
        return res
                
                
                
        