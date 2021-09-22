class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res, ct_curr, ct_second = 0, 0, 0 
        first, second = 0, 0
        for fruit in fruits:
            if fruit in (first, second):
                ct_curr += 1
            else:
                ct_curr = ct_second + 1
                
            if fruit != second:
                first, second = second, fruit
                ct_second = 1
            else:
                ct_second += 1
                
            res = max(res, ct_curr)
            
        return res