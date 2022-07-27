class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def mul(single, b):
            res = 0
            r = (ord(single) - ord("0"))
            for c in b:
                res = 10 * res +  r * (ord(c) - ord("0"))
            return res
        res = 0
        for num in num1:
            res = 10 * res + mul(num, num2)
        return str(res)
            
                