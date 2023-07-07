class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res, ct, ct_2 = 0, 0, 0
        first, second = -1, -1
        
        for fruit in fruits:
            if fruit not in (first, second):
                ct = ct_2 + 1
            else:
                ct += 1
            
            if fruit == second:
                ct_2 += 1
            else:
                first, second = second, fruit
                ct_2 = 1
            
            res = max(res, ct)
        return res