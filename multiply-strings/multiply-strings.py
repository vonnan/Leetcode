class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(num):
            res = 0
            for s in num:
                res = res*10 + ord(s) - ord("0")
            return res
        
        return str(convert(num1) * convert(num2))
                