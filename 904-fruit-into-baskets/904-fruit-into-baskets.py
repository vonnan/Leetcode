class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res, ct, ct_second = 0, 0, 0
        first, second = 0, 0
        
        for fruit in fruits:
            if fruit in (first, second):
                ct += 1
            else:
                ct = ct_second + 1
                
            if fruit == second:
                ct_second += 1
            else:
                ct_second = 1
                first, second = second, fruit
                
            res = max(res, ct)
            
        return res
                
                    
            