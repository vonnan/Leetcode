
class Solution:
    def numberOfWeakCharacters(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x: (-x[0], x[1]))
        res = 0
        curr_max = 0
        
        for _, a in A:   
            curr_max = max(curr_max, a)
            if a < curr_max:
                res += 1
        
        return res
                
                
        
        
        
                
                
            
            
        
        