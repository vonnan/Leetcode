class Solution:
    def findIntegers(self, num: int) -> int:
        a, b = 1, 2
        num += 1
        res = 0
        
        while num:
            if num & 1 and num & 2:
                res = 0
            
            res += a * (num & 1)
            print(num, a,b, num & 1, res)
            num >>= 1
            
            a, b = b, a + b
        return res
            